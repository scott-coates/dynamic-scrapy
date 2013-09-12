import logging

from django.db import models

from scrapy_test.libs.common_domain.aggregate_base import AggregateBase

logger = logging.getLogger(__name__)


class Result(models.Model, AggregateBase):

  def __unicode__(self):
    return 'Result #' + str(self.pk)
