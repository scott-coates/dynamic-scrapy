import logging
from django.core.exceptions import ValidationError

from django.db import models, transaction
import jsonfield
from localflavor.us.models import USStateField, PhoneNumberField
import reversion
from scrapy_test.aggregates.listing.managers import ListingManager

from scrapy_test.aggregates.listing.signals import created, sanitized, deleted, unsanitized
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.django_utils.models.utils import copy_django_model_attrs
from scrapy_test.libs.common_domain.models import RevisionEvent
from scrapy_test.libs.geo_utils.parsing import address_parser


logger = logging.getLogger(__name__)


class Listing(models.Model, AggregateBase):
  #todo put in unique constraints (zip, lat, lng, etc)
  def __init__(self, *args, **kwargs):
    super(Listing, self).__init__(*args, **kwargs)
    self._amenity_list = []

  objects = ListingManager()

  listing_source = models.ForeignKey(ListingSource)

  title = models.CharField(max_length=8000)
  description = models.TextField()
  posted_date = models.DateTimeField()
  last_updated_date = models.DateTimeField()
  url = models.URLField()

  address = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  formatted_address = models.CharField(max_length=4096)

  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  broker_fee = models.BooleanField()

  contact_name = models.CharField(max_length=255, blank=True, null=True)
  contact_phone_number = PhoneNumberField(blank=True, null=True)
  contact_email_address = models.EmailField(blank=True, null=True)

  requires_sanity_checking = models.BooleanField()
  validation_parsing_errors = jsonfield.JSONField(blank=True, null=True)

  apartment = models.ForeignKey('apartment.Apartment', related_name='listings', blank=True, null=True)

  #is the listing actually viewable on an external website?
  is_alive = models.BooleanField()
  #did we manually delete this?
  is_deleted = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)


  @classmethod
  def _from_attrs(cls, **kwargs):
    #todo some validation should go here and in the command handler (zip code validation, etc)
    ret_val = cls()

    if not kwargs.get('listing_source_id'): raise TypeError('listing source id is required')

    price = kwargs.get('price')
    if not price:
      raise TypeError("price is required")
    elif price < .01:
      raise ValidationError("price is not valid: {0}".format(price))

    lat = kwargs.get('lat')
    if not lat:
      raise TypeError("lat is required")
    elif lat < .01:
      raise ValidationError("lat is not valid: {0}".format(lat))

    lng = kwargs.get('lng')
    if not lng:
      raise TypeError("lng is required")
    elif price < .01:
      raise ValidationError("lng is not valid: {0}".format(lng))

    zip_code = kwargs.get('zip_code')
    if not zip_code:
      raise TypeError("zip_code is required")
    elif not address_parser.is_valid_zip_code(zip_code):
      raise ValidationError("zip_code is not valid: {0}".format(zip_code))

    ret_val._raise_event(created, sender=Listing, instance=ret_val, attrs=kwargs)

    ret_val.reset_sanitization_status()

    return ret_val

  def reset_sanitization_status(self):
    errors = {}
    if not self.address1:
      errors["address"] = ["Missing address1"]

    if not self.price:
      errors["price"] = ["Missing price"]

    if not self.contact_phone_number and not self.contact_email:
      errors["communication"] = ["Missing phone and email"]

    if not self.description:
      errors["description"] = ["Missing description"]
    elif len(self.description) < 20:
      errors["description"] = ["Description too short"]

    if not self.last_updated_date:
      errors["last updated date"] = ["Missing last updated date"]

    if not self.posted_date:
      errors["posted date"] = ["Missing posted date"]

    if errors:
      self.make_unsanitized(errors)
      if len(errors) >= 5:
        self.make_deleted()
    else:
      self.make_sanitized()

  def make_sanitized(self):
    self._raise_event(sanitized, sender=Listing, instance=self)

  def make_unsanitized(self, errors):
    self._raise_event(unsanitized, sender=Listing, errors=errors, instance=self)

  def make_deleted(self):
    self._raise_event(deleted, sender=Listing, instance=self)

  #region event handlers

  def _handle_created_event(self, **kwargs):
    amenities = kwargs['attrs'].pop('amenities', None)
    if amenities:
      self._amenity_list.extend(amenities)

    # django model constructor has pretty smart logic for mass assignment
    copy_django_model_attrs(self, **kwargs['attrs'])

    logger.info("{0} has been created".format(self))

  def _handle_deleted_event(self, **kwargs):
    self.is_deleted = True
    logger.info("{0} has been marked as deleted".format(self))

  def _handle_sanitized_event(self, **kwargs):
    logger.info("{0} has been marked as sanitized".format(self))

  def _handle_unsanitized_event(self, **kwargs):
    errors = kwargs.get('errors')
    self.validation_parsing_errors = errors
    self.requires_sanity_checking = True

    logger.info("{0} has been marked as unsanitized".format(self))

  #endregion

  def __unicode__(self):
    return 'Listing #' + str(self.pk) + ': ' + self.formatted_address


  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        with reversion.create_revision():
          super(Listing, self).save(*args, **kwargs)

          for a in self._amenity_list:
            #add actually does a save internally, hitting the db
            self.amenities.add(a)

          for event in self._uncommitted_events:
            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version)

      self.send_events()
    else:
      from scrapy_test.aggregates.listing.services import listing_service

      listing_service.save_or_update(self)


class Amenity(models.Model):
  is_available = models.BooleanField()
  listing = models.ForeignKey(Listing, related_name='amenities')
  amenity_type = models.ForeignKey('amenity.Amenity', related_name='listing_instance')

  class Meta:
    unique_together = ("listing", "amenity_type")
