import logging
import os

from django.db import models, transaction
import reversion
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.result.signals import created_from_apartment_and_search

from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.common_domain.models import RevisionEvent

logger = logging.getLogger(__name__)


class Result(models.Model, AggregateBase):
  apartment = models.ForeignKey('apartment.Apartment', related_name="results")

  search = models.ForeignKey('search.Search', related_name="results")

  compliance_score = models.PositiveSmallIntegerField(max_length=2)

  created = models.DateTimeField(auto_now_add=True)
  changed = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ("apartment", "search")

  @classmethod
  def _from_apartment_and_search(cls, apartment, search):
    ret_val = cls()

    if not apartment:
      raise TypeError("apartment is required")

    if not search:
      raise TypeError("search is required")

    ret_val._raise_event(
      created_from_apartment_and_search,
      sender=Result,
      instance=ret_val,
      apartment=apartment,
      search=search
    )

    return ret_val

  def _handle_created_from_apartment_and_search_event(self, apartment, search, **kwargs):
    numerator = 0.0
    denominator = 0.0
    for attr in Apartment._meta.get_all_field_names():

      search_attr = attr.rstrip('_count')

      if attr in ('bedroom_count', 'bathroom_count', 'price'):
        denominator += 1
        # if the number of beds or baths is greater than what is requested, this is fine
        if getattr(apartment, attr) is not None and attr in ('bedroom_count', 'bathroom_count'):
          if getattr(apartment, attr) >= getattr(search, search_attr + '_min'):
            numerator += 1
        # if the price is less than what is requested, this is fine
        elif getattr(apartment, attr) and attr == 'price':
          if getattr(apartment, attr) <= getattr(search, search_attr + '_max'):
            numerator += 1

      # If there is a square footage, and it is within the range, increment denominator and numerator. If no square
      # footage, do nothing.
      elif attr == 'sqfeet':
        if getattr(apartment, attr) is not None:
          denominator += 1
          if getattr(apartment, attr) >= getattr(search, search_attr + '_min'):
            numerator += 1

      # Necessary so that, if there are more perks than requested, this will not count against or help the compliance
      #  level
      elif attr == 'amenities':
        amenities_count = getattr(search, search_attr).count()
        if amenities_count:
          denominator += amenities_count
          for val in getattr(search, search_attr).all().values_list('amenity_type__id', flat=True):
            for attr_val in getattr(apartment, attr).values_list('amenity_type__id', 'is_available'):
              if attr_val[0] == val and attr_val[1]:
                numerator += 1

    self.compliance_score = int(round(numerator / denominator, 2) * 100)

    logger.info(
      "Calculated compliance for result: {0}.{sep}"
      "Apartment: {1}.{sep}"
      "Search: {2}.{sep}"
      "Score: {3}".format(self, apartment, search, self.compliance_score, sep=os.linesep))


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
