from dynamic_scraper.models import Scraper
from dynamic_scraper.spiders.django_spider import DjangoSpider
from dynamic_scraper.utils.processors import string_strip
from scrapy.contrib.loader.processor import TakeFirst, Identity
from scrapy.http import Request
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.apps.web_scraper.models import ListingScrapyItem, ListingSourceScraperConfig


class ListingSpider(DjangoSpider):
  name = 'listing_spider'

  def __init__(self, *args, **kwargs):
    if not hasattr(self, 'ref_object'): self._set_ref_object(ListingSourceScraperConfig, **kwargs)
    if not hasattr(self, 'scraper'): self.scraper = self.ref_object.scraper
    if not hasattr(self, 'scrape_url'): self.scrape_url = self.ref_object.listing_source.url
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

  def parse_item(self, response, xs=None):

    #multi-detail-hack
    #if a previous request is the beginning of a multi-detail scrape, we need to store that scraper as temp variable
    # because this page will use its own scraper to load the details from this page
    temp_scraper = None
    pre_defined_scraper = response.meta.pop('scraper', None)

    if (pre_defined_scraper):
      temp_scraper = self.scraper
      self.scraper = pre_defined_scraper

    parsed_item = super(ListingSpider, self).parse_item(response, xs)

    if pre_defined_scraper:
      self.scraper = temp_scraper
      ret_val = parsed_item
    else:
      # some sites like streeteasy have the lstings spread over manyy differnt pages and DDS will not natively work
      # that way. To get around it, we'll not return the parsed item just yet. We'll hand off a request to parse the
      # next page in this multi-detail scrape.
      if self.from_detail_page and 'streeteasy' in response.url:

        scraper = Scraper.objects.get(name='StreetEasy Contact Page Partial-Listing Scraper')

        ret_val = Request(
          parsed_item['contact_name'][0], callback=self.parse_item, meta={
            'item': parsed_item,
            'scraper': scraper
          }
        )
      else:
        ret_val = parsed_item

    return ret_val

