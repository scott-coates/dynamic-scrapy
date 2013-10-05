from datetime import timedelta
from django.dispatch import receiver
from django.utils import timezone
from scrapy import signals
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.apps.web_scraper.spiders.listing_spider import ListingSpider
from scrapy_test.libs.analytics_utils.services import analytics_service
from scrapy_test.libs.datetime_utils.parsers import datetime_parser
from scrapy_test.libs.geo_utils.signals import location_geocoded


class StopOnDuplicateItem(object):
  def __init__(self, crawler):
    self.crawler = crawler

    crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)

  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler)

  def item_scraped(self, item, spider):
    url = item['url']
    if url[0:6] == 'DOUBLE':
      duplicate = Listing.objects.filter(url=url[6:]).get()

      if timezone.now() - duplicate.created_date >= timedelta(hours=1):
        # if this listing is being crawled again, but we just recently created it,
        # don't stop crawling. This could happen if
        # we first encounter it on page 100.html but new posts appeared and forced this to 200.html, the next page.

        #get first item in last_updated_date or None
        if next((datetime_parser.get_datetime(x) for x in item['last_updated_date']), None) == \
            duplicate.last_updated_date:
        # if this listing was created a long time ago but just recently re-newed or re-updated.

          if timezone.now() - duplicate.changed >= timedelta(hours=1):
            # This might happen if a listing was added a long time ago but then was re-posted today. Then we started
            # crawling and stumbled upon this listing and it was on, say, page 100.html. So we update the
            # last_updated_date to today. As we reach 200.html, this SAME, listing appears again because new posts
            # pushed
            # it from page 100.html to page 200.html. If we now see it again, we know we still have to keep crawling.
            # However, we should inspect something other than listing.changed because changed could be updated from the
            # admin and would cause us to continue parsing even though we should've stopped. So we could perhaps store
            # that value in the last_updated_date_recorded_datetime prop. But the likelihood of that happening is rare
            # because we'd need to manually modify a listing minutes after it shows up as a re-post.

            self.crawler.engine.close_spider(spider, 'duplicate listing found: {0}'.format(url))


class StatsReporter(object):
  interested_stats = ['item_dropped', 'location_geocoded']

  def __init__(self, crawler, analytics_service=analytics_service):
    self.crawler = crawler
    self._analytics_service = analytics_service

    @receiver(location_geocoded, weak=False)
    def location_geocoded_callback(sender, **kwargs):
      self.crawler.stats.inc_value('location_geocoded')

    crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler)

  def spider_closed(self, spider):
    stats = self.crawler.stats.get_stats()

    stats_to_log = {key: value for key, value in stats.items() if
                    any(key.lower().startswith(item) for item in StatsReporter.interested_stats)}

    stats_to_log['spider_name'] = spider.name

    if isinstance(spider, ListingSpider):
      stats_to_log['listing_source_name'] = spider.ref_object.listing_source.name
      stats_to_log['listing_source_url'] = spider.ref_object.listing_source.url

    self._analytics_service.send_event("Crawler Finished", **stats_to_log)
