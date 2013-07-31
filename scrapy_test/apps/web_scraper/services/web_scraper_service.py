from dynamic_scraper.models import SchedulerRuntime
from dynamic_scraper.utils.task_utils import ProcessBasedUtils
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.apps.web_scraper.models import ListingSourceScraperConfig, ListingCheckerConfig


def run_spiders():
  t = ProcessBasedUtils()
  t.run_spiders(ListingSourceScraperConfig, 'scraper', 'scraper_runtime', 'listing_spider')


def add_listing_checker(listing_id):
  listing = listing_service.get_listing(listing_id)

  checker_rt = SchedulerRuntime(runtime_type='C')
  checker_rt.save()

  checker_config = ListingCheckerConfig(listing=listing, checker_runtime=checker_rt)
  checker_config.save()

  return checker_config
