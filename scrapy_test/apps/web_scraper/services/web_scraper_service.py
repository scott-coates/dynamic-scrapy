from dynamic_scraper.utils.task_utils import TaskUtils
from scrapy_test.aggregates.listing_source.models import ListingSource


def run_spiders():
  t = TaskUtils()
  t.run_spiders(ListingSource, 'scraper', 'scraper_runtime', 'listing_spider')
