from django.db import models
import logging
import jsonfield
from localflavor.us.models import USStateField, PhoneNumberField
from scrapy_test.aggregates.listing.signals import listing_deleted, listing_sanitized
from scrapy_test.aggregates.listing_source.models import ListingSource

logger = logging.getLogger(__name__)


class Listing(models.Model):
  listing_source = models.ForeignKey(ListingSource)

  title = models.CharField(max_length=8000)
  description = models.TextField()
  last_updated_date = models.DateTimeField()
  url = models.URLField()

  address1 = models.CharField(max_length=255, blank=True, null=True)
  address2 = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()

  bedroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  broker_fee = models.BooleanField()

  contact_name = models.CharField(max_length=255, blank=True, null=True)
  contact_phone_number = PhoneNumberField(blank=True, null=True)
  contact_email = models.EmailField(blank=True, null=True)

  requires_sanity_checking = models.BooleanField()
  validation_parsing_errors = jsonfield.JSONField(blank=True, null=True)

  # apartment    = models.ForeignKey('apartment.Apartment', related_name='listings', blank=True, null=True)
  #
  # crawl    = models.ForeignKey('crawl.Crawl', related_name='listings', blank=True, null=True)
  #
  # amenities = dbarray.TextArrayField(blank=True, null=True)
  # pets               = models.ManyToManyField('pet.Pet',                          blank=True, null=True)
  # building_amenities = models.ManyToManyField('building_amenity.BuildingAmenity', blank=True, null=True)
  # building_types     = models.ManyToManyField('building_type.BuildingType',       blank=True, null=True)
  # unit_amenities     = models.ManyToManyField('unit_amenity.UnitAmenity',         blank=True, null=True)
  # unit_types         = models.ManyToManyField('unit_type.UnitType',               blank=True, null=True)

  #is the listing actually viewable on an external website?
  is_alive = models.BooleanField()
  #did we manually delete this?
  is_deleted = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def reset_sanitization_status(self):
    errors = {}
    if not self.address1:
      errors["address1"] = ["Missing address"]

    if not self.price:
      errors["price"] = ["Missing price"]

    if not self.phone_number and not self.email:
      errors["communication"] = ["Missing phone and email"]

    if not self.description:
      errors["description"] = ["Missing description"]
    elif len(self.description) < 20:
      errors["description"] = ["Description too short"]

    if not self.last_updated:
      errors["last updated"] = ["Missing last updated date"]

    if errors:
      self.validation_parsing_errors = errors
      self.requires_sanity_checking = True

      if len(errors) >= 5:
        self.make_deleted()
    else:
      listing_sanitized.send(sender=self)

  def make_deleted(self):
    logger.info("{0} has been marked as deleted".format(self))
    self.is_deleted = True
    listing_deleted.send(sender=self)

  def __unicode__(self):
    return self.title

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Listing, self).save(*args, **kwargs)
    else:
      from scrapy_test.aggregates.listing.services import listing_service

      listing_service.save_or_update(self)
