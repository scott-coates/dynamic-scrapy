from django.db import models
import logging
from localflavor.us.models import USStateField
from scrapy_test.aggregates.apartment.managers import ApartmentManager
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase

logger = logging.getLogger(__name__)


class Apartment(models.Model, AggregateBase):
  #todo create unique constraint for lat, lng price
  objects = ApartmentManager()

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

  #can this apartment be rented?
  is_available = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def adopt_listing(self, listing):
    self.listings.add(listing)

  def __unicode__(self):
    return 'Apartment #' + str(self.pk) + ': ' + self.formatted_address

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Apartment, self).save(*args, **kwargs)
      self.send_events()
    else:
      from scrapy_test.aggregates.apartment.services import apartment_service

      apartment_service.save_or_update(self)
