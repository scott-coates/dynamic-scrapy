import traceback
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy_test.aggregates.listing.services import listing_tasks
from scrapy_test.apps.web_scraper.services import web_scraper_tasks


class AggregateCommandPipeline(object):
  def process_item(self, item, spider):
    try:

      if item['url'][0:6] == 'DOUBLE':
        item['url'] = item['url'][6:]
        listing_tasks.create_listing_task.delay(**dict(item, listing_source_id=spider.ref_object.listing_source.id))
      else:
        listing_tasks.create_listing_task.delay(**dict(item, listing_source_id=spider.ref_object.listing_source.id))

      spider.action_successful = True
      spider.log("Listing item sent to application to be processed.", log.INFO)
    except:
      spider.log(traceback.format_exc(), log.ERROR)
      raise DropItem("Error sending listing item.")

    return item
