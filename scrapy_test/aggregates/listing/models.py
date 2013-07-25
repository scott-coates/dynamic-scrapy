from django.db import models
import logging
from dynamic_scraper.models import SchedulerRuntime
from scrapy_test.aggregates.listing_source.models import ListingSource

logger = logging.getLogger(__name__)

class Listing(models.Model):
  title = models.CharField(max_length=200)
  listing_source = models.ForeignKey(ListingSource)
  description = models.TextField(blank=True)
  url = models.URLField()

  def __unicode__(self):
    return self.title
