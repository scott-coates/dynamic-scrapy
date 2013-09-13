import logging

from django.db import models, transaction
import reversion

from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.common_domain.models import RevisionEvent

logger = logging.getLogger(__name__)


class Result(models.Model, AggregateBase):
  apartment = models.ForeignKey('apartment.Apartment', related_name="results")

  search = models.ForeignKey('search.Search', related_name="results")

  compliance = models.PositiveSmallIntegerField(max_length=2)

  created = models.DateTimeField(auto_now_add=True)
  changed = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ("apartment", "search")

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        with reversion.create_revision():
          super(Result, self).save(*args, **kwargs)

          for event in self._uncommitted_events:
            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version)

      self.send_events()
    else:
      from scrapy_test.aggregates.result.services import result_service

      result_service.save_or_update(self)

  def __unicode__(self):
    return 'Result #' + str(self.pk)
