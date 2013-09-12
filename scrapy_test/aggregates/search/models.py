from django.db import models
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase


class Search(models.Model, AggregateBase):
  description = models.TextField()

  specified_location = models.CharField(max_length=2048)
  lat = models.FloatField()
  lng = models.FloatField()

  no_fee_preferred = models.BooleanField()

  bedroom_min = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bedroom_max = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  bathroom_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  price_min = models.DecimalField(max_digits=10, decimal_places=2)
  price_max = models.DecimalField(max_digits=10, decimal_places=2)
  sqfeet_min = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
  sqfeet_max = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
