from datetime import timedelta
from django.utils import timezone
from scrapy import signals
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.datetime_utils.parsers import datetime_parser


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
  def __init__(self, crawler):
    self.crawler = crawler

    crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler)

  def spider_closed(self, spider):
    #get the stats
    stats = self.crawler.stats.get_stats()
    stats_to_log = {key: value for key, value in stats.items() if key.startswith('item_dropped')}
    pass
