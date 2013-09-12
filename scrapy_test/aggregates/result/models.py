import logging

from django.db import models

from scrapy_test.libs.common_domain.aggregate_base import AggregateBase

logger = logging.getLogger(__name__)


class Result(models.Model, AggregateBase):
  apartment = models.ForeignKey('apartment.Apartment', related_name="results")

  search = models.ForeignKey('search.Search', related_name="results")

  compliance = models.PositiveSmallIntegerField(max_length=2)

  created = models.DateTimeField(auto_now_add=True)
  changed = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return 'Result #' + str(self.pk)
