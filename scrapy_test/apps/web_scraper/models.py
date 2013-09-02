#http://stackoverflow.com/a/1224760/173957
#scrapy must refer to the third party package, Scrapy
from __future__ import absolute_import
from django.db import models
from dynamic_scraper.models import SchedulerRuntime, Scraper
from scrapy.contrib.djangoitem import DjangoItem
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing_source.models import ListingSource


class ListingScrapyItem(DjangoItem):
  django_model = Listing


class ListingSourceScraperConfig(models.Model):
  listing_source = models.OneToOneField(ListingSource, primary_key=True, related_name='scraper_config')
  scraper = models.OneToOneField(Scraper)
  scraper_runtime = models.OneToOneField(SchedulerRuntime)

  def __unicode__(self):
    return self.listing_source.name

  def delete(self, using=None):
    self.scraper_runtime.delete()
    super(ListingSourceScraperConfig, self).delete(using)


class ListingCheckerConfig(models.Model):
  listing = models.OneToOneField(Listing, primary_key=True, related_name='checker_config')
  checker_runtime = models.OneToOneField(SchedulerRuntime)
  scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)

  def __unicode__(self):
    return str(self.listing)

  def delete(self, using=None):
    self.checker_runtime.delete()
    super(ListingCheckerConfig, self).delete(using)

