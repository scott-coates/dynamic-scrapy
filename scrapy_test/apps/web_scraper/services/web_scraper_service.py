from dynamic_scraper.models import SchedulerRuntime
from dynamic_scraper.utils.task_utils import ProcessBasedUtils
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.apps.web_scraper.models import ListingSourceScraperConfig, ListingCheckerConfig
from scrapy_test.apps.web_scraper.scrapy.task_utils import IndividualProcessBasedItemLauncher


def run_spiders():
  t = ProcessBasedUtils()
  t.run_spiders(ListingSourceScraperConfig, 'scraper', 'scraper_runtime', 'listing_spider')

def run_checkers():
  t = ProcessBasedUtils()
  t.run_checkers(ListingCheckerConfig, 'scraper', 'checker_runtime', 'listing_checker')

def run_individual_listing_spider(url):
  t = IndividualProcessBasedItemLauncher()
  t.run_spider('individual_listing_spider', url)


def add_listing_checker(listing):
  listing_source_cfg = ListingSourceScraperConfig.objects.get(pk=listing.listing_source_id)

  checker_rt = SchedulerRuntime(runtime_type='C')
  checker_rt.save()

  checker_config = ListingCheckerConfig(listing=listing, checker_runtime=checker_rt, scraper=listing_source_cfg.scraper)
  checker_config.save()

  return checker_config
