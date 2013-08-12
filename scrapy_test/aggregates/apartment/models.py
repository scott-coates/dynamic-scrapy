from django.db import models
import logging
from localflavor.us.models import USStateField
from scrapy_test.aggregates.apartment.managers import ApartmentManager
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase

logger = logging.getLogger(__name__)


class Apartment(models.Model, AggregateBase):
  #todo create unique constraint for lat, lng price
  objects = ApartmentManager()

  address1 = models.CharField(max_length=255, blank=True, null=True)
  address2 = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()

  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  broker_fee = models.BooleanField()

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

  #can this apartment be rented?
  is_available = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def adopt_listing(self, listing):
    self.listings.add(listing)

  def __unicode__(self):
    return ('Apartment #' + str(self.pk) + ': ' + str(self.address1 or '') + " (" + str(self.city or '') + ", " +
            str(self.state or '') + ")")

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Apartment, self).save(*args, **kwargs)
      self.send_events()
    else:
      from scrapy_test.aggregates.apartment.services import apartment_service

      apartment_service.save_or_update(self)
