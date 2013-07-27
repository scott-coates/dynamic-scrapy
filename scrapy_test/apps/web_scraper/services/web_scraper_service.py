from dynamic_scraper.utils.task_utils import ProcessBasedUtils
from scrapy_test.apps.web_scraper.models import ListingSourceScraperConfig


def run_spiders():
  t = ProcessBasedUtils()
  t.run_spiders(ListingSourceScraperConfig, 'scraper', 'scraper_runtime', 'listing_spider')
