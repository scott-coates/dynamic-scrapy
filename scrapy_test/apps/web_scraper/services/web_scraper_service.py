from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.apps.web_scraper.scrapy_extensions.utils_extensions import ProcessBasedUtils


def run_spiders():
  t = ProcessBasedUtils()
  t.run_spiders(ListingSource, 'scraper', 'scraper_runtime', 'listing_spider')
