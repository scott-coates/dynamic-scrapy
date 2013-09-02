import traceback
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy_test.aggregates.listing.services import listing_tasks
from scrapy_test.apps.web_scraper.spiders.listing_spider import ListingSpider


class AggregateCommandPipeline(object):
  def process_item(self, item, spider):
    try:
      double = item['url'][0:6] == 'DOUBLE'
      if double:
        item['url'] = item['url'][6:]

      if isinstance(spider, ListingSpider):
        if double:
          listing_tasks.update_listing_task.delay(**dict(item, listing_source_id=spider.ref_object.listing_source.id))
        else:
          listing_tasks.create_listing_task.delay(**dict(item, listing_source_id=spider.ref_object.listing_source.id))

      spider.action_successful = True
      spider.log("Iitem sent to application to be processed.", log.INFO)
    except:
      spider.log(traceback.format_exc(), log.ERROR)
      raise DropItem("Error sending item.")

    return item
