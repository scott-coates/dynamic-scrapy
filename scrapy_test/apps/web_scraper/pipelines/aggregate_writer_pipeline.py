from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from scrapy_test.apps.web_scraper.models import ListingCheckerConfig


class AggregateCommandPipeline(object):
  def process_item(self, item, spider):
    try:
      item['listing_source'] = spider.ref_object.listing_source

      checker_rt = SchedulerRuntime(runtime_type='C')
      checker_rt.save()


      listing_model = item.save()

      checker_config = ListingCheckerConfig(listing=listing_model,checker_runtime=checker_rt)
      checker_config.save()

      spider.action_successful = True
      spider.log("Item saved.", log.INFO)

    except IntegrityError, e:
      spider.log(str(e), log.ERROR)
      raise DropItem("Missing attribute.")

    return item
