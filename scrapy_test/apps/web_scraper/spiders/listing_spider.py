from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.apps.web_scraper.model_proxies import ListingItem


class ListingSpider(DjangoSpider):
  name = 'listing_spider'

  def __init__(self, *args, **kwargs):
    self._set_ref_object(ListingSource, **kwargs)
    self.scraper = self.ref_object.scraper
    self.scrape_url = self.ref_object.url
    self.scheduler_runtime = self.ref_object.scraper_runtime
    self.scraped_obj_class = Listing
    self.scraped_obj_item_class = ListingItem
    super(ListingSpider, self).__init__(self, *args, **kwargs)
