from dynamic_scraper.spiders.django_spider import DjangoSpider
from dynamic_scraper.utils.processors import string_strip
from scrapy.contrib.loader.processor import TakeFirst, Identity
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.apps.web_scraper.models import ListingScrapyItem, ListingSourceScraperConfig


class ListingSpider(DjangoSpider):
  name = 'listing_spider'

  def __init__(self, *args, **kwargs):
    if not self.ref_object: self._set_ref_object(ListingSourceScraperConfig, **kwargs)
    if not self.scraper: self.scraper = self.ref_object.scraper
    if not self.scrape_url: self.scrape_url = self.ref_object.listing_source.url
    self.scheduler_runtime = self.ref_object.scraper_runtime
    self.scraped_obj_class = Listing
    self.scraped_obj_item_class = ListingScrapyItem
    super(ListingSpider, self).__init__(self, *args, **kwargs)

  def _get_processors(self, procs_str):
    procs = super(ListingSpider, self)._get_processors(procs_str)
    procs = [p for p in procs if not (isinstance(p, TakeFirst) or p == string_strip)]
    return tuple(procs)

  def _set_loader(self, response, xs, item):
    super(ListingSpider, self)._set_loader(response, xs, item)
    self.loader.default_output_processor = Identity()
    self.loader.url_out = TakeFirst()
