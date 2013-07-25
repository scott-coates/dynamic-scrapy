from scrapy_test.apps.web_scraper.models import ListingSourceScraperConfig
from scrapy_test.apps.web_scraper.scrapy_extensions.utils_extensions import ProcessBasedUtils


def run_spiders():
  t = ProcessBasedUtils()
  t.run_spiders(ListingSourceScraperConfig, 'scraper', 'scraper_runtime', 'listing_spider')
