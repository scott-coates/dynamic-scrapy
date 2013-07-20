from dynamic_scraper.spiders.django_spider import DjangoSpider
from dynamic_scraper.utils import processors
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.apps.web_scraper.model_proxies import ListingItem


def pre_url_from_ref_object(text, loader_context):
  from urlparse import urljoin

  base_url = loader_context['spider'].ref_object.url

  ret_val = urljoin(base_url, text)

  return ret_val


setattr(processors, 'pre_url_from_ref_object', pre_url_from_ref_object)


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
