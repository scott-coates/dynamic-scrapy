from scrapy import signals
from scrapy_test.aggregates.listing.models import Listing


class StopOnDuplicateItem(object):
  def __init__(self, crawler):
    self.crawler = crawler

    crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)

  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler)

  def item_scraped(self, item, spider):
    url = item['url']
    duplicate = Listing.objects.filter(url=url).count() > 0
    if duplicate:
      self.crawler.engine.close_spider(spider, 'duplicate listing found: {0}'.format(url))
