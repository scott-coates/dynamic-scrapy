from dynamic_scraper.spiders.django_checker import DjangoChecker
from scrapy_test.apps.web_scraper.models import ListingCheckerConfig


class ListingChecker(DjangoChecker):
  name = 'listing_checker'

  def __init__(self, *args, **kwargs):
    self._set_ref_object(ListingCheckerConfig, **kwargs)
    self.scraper = self.ref_object.scraper
    self.scrape_url = self.ref_object.listing.url
    self.scheduler_runtime = self.ref_object.checker_runtime
    super(ListingChecker, self).__init__(self, *args, **kwargs)
