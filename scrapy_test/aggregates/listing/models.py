from django.db import models
import logging
from dynamic_scraper.models import SchedulerRuntime
from scrapy_test.aggregates.listing_source.models import ListingSource

logger = logging.getLogger(__name__)

class Listing(models.Model):
  title = models.CharField(max_length=200)
  listing_website = models.ForeignKey(ListingSource)
  description = models.TextField(blank=True)
  url = models.URLField()
  checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

  def __unicode__(self):
    return self.title
