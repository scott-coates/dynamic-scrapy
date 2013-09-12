from django.db import models
from localflavor.us.models import USStateField

from scrapy_test.libs.common_domain.aggregate_base import AggregateBase


class Search(models.Model, AggregateBase):
  description = models.TextField()

  specified_location = models.CharField(max_length=2048)

  address = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  formatted_address = models.CharField(max_length=4096)

  no_fee_preferred = models.BooleanField()

  bedroom_min = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bedroom_max = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  bathroom_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  price_min = models.DecimalField(max_digits=10, decimal_places=2)
  price_max = models.DecimalField(max_digits=10, decimal_places=2)
  sqfeet_min = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
  sqfeet_max = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

  def __unicode__(self):
    return 'Search #' + str(self.pk) + ': ' + self.formatted_address

class Amenity(models.Model):
  is_available = models.BooleanField()
  apartment = models.ForeignKey(Search, related_name='amenities')
  amenity_type = models.ForeignKey('amenity.Amenity', related_name='search_instance')

  class Meta:
    unique_together = ("search", "amenity_type")
