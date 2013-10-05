from datetime import datetime
import logging
from django.core.exceptions import ValidationError

from django.db import models, transaction
from django.utils import timezone
from localflavor.us.models import USStateField, PhoneNumberField
import reversion
from scrapy_test.aggregates.listing.enums import DeletedListingReasonChoices, DeletedListingReasonEnum
from scrapy_test.aggregates.listing.managers import ListingManager

from scrapy_test.aggregates.listing.signals import created, deleted, updated_last_updated_date, \
  associated_with_apartment
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.django_utils.models.utils import copy_django_model_attrs
from scrapy_test.libs.common_domain.models import RevisionEvent
from scrapy_test.libs.django_utils.serialization.flexible_json_serializer import JSONSerializer
from scrapy_test.libs.geo_utils.parsing import address_parser


logger = logging.getLogger(__name__)


class Listing(models.Model, AggregateBase):
  objects = ListingManager()

  listing_source = models.ForeignKey(ListingSource)

  title = models.CharField(max_length=8000)
  description = models.TextField()
  posted_date = models.DateTimeField()
  last_updated_date = models.DateTimeField(blank=True, null=True)
  url = models.URLField(unique=True)

  address = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  formatted_address = models.CharField(max_length=4096)

  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  broker_fee = models.BooleanField()

  contact_name = models.CharField(max_length=255, blank=True, null=True)
  contact_phone_number = PhoneNumberField(blank=True, null=True)
  contact_email_address = models.EmailField(blank=True, null=True)

  apartment = models.ForeignKey('apartment.Apartment', related_name='listings', blank=True, null=True)

  is_deleted = models.BooleanField()
  #dead link? notified unavailable? admin deleted it?
  deleted_reason = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True,
                                                    choices=DeletedListingReasonChoices)

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def __init__(self, *args, **kwargs):
    super(Listing, self).__init__(*args, **kwargs)
    self._amenity_list = []

  @classmethod
  def _from_attrs(cls, **kwargs):
    ret_val = cls()

    if not kwargs.get('listing_source'): raise TypeError('listing source is required')

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

    posted_date = kwargs.get('posted_date')
    if not posted_date:
      raise TypeError("posted_date is required")
    ret_val._validate_listing_date(posted_date)

    last_updated_date = kwargs.get('last_updated_date')
    if last_updated_date:
      ret_val._validate_listing_date(last_updated_date)
      if not last_updated_date > posted_date:
        raise ValidationError("posted_date must be before last_updated_date")

    communication = kwargs.get('contact_phone_number', kwargs.get('contact_email_address', None))
    if not communication:
      raise ValidationError("contact_phone_number or contact_email_address is required")

    ret_val._raise_event(created, sender=Listing, instance=ret_val, attrs=kwargs)

    return ret_val

  def _validate_listing_date(self, last_updated_date):
    if not isinstance(last_updated_date, datetime):
      raise TypeError("Provided date must be a datetime type")

    if timezone.is_naive(last_updated_date):
      raise ValidationError("Provided date must have a timezone")

  def update_last_updated_date(self, last_updated_date):
    self._validate_listing_date(last_updated_date)

    self._raise_event(updated_last_updated_date, sender=Listing, last_updated_date=last_updated_date, instance=self)

  def notify_unavailable(self):
    self._raise_event(deleted, sender=Listing, instance=self, reason=DeletedListingReasonEnum.NotifiedUnavailable)

  def make_dead(self):
    self._raise_event(deleted, sender=Listing, instance=self, reason=DeletedListingReasonEnum.DeadListing)

  def associate_with_apartment(self, apartment):
    self._raise_event(associated_with_apartment, sender=Listing, instance=self, apartment=apartment)

    #region event handlers

  def _handle_created_event(self, **kwargs):
    amenities = kwargs['attrs'].pop('amenities', None)
    if amenities:
      self._amenity_list.extend(Amenity(amenity_type_id=a.keyword_id, is_available=a.is_available) for a in amenities)

    # django model constructor has pretty smart logic for mass assignment
    copy_django_model_attrs(self, **kwargs['attrs'])

    logger.info("{0} has been created".format(self))

  def _handle_deleted_event(self, **kwargs):
    self.is_deleted = True
    self.deleted_reason = kwargs['reason']
    logger.info("{0} has been marked as deleted".format(self))

  def _handle_updated_last_updated_date_event(self, last_updated_date, **kwargs):
    self.last_updated_date = last_updated_date
    logger.info("{0} last_updated_date set to {1}".format(self, last_updated_date))

  def _handle_associated_with_apartment_event(self, apartment, **kwargs):
    self.apartment = apartment
    logger.info("{0} has been associated with {1}".format(self, apartment))

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

          serializer = JSONSerializer()

          for event in self._uncommitted_events:
            #we don't need to store the instance because it's not really part of the parameters
            #and django-reversion will keep a snapshop
            kwargs_to_save = {k: v for k, v in event.kwargs.items() if k != 'instance'}

            data = serializer.serialize(kwargs_to_save)

            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version, data=data)

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
