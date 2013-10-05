from urlparse import urlparse
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.apps.web_scraper.spiders.individual_item_spider import IndividualItemSpider
from scrapy_test.apps.web_scraper.spiders.listing_spider import ListingSpider
from scrapy_test.libs.text_utils.search import fuzzy_search


class IndividualListingSpider(IndividualItemSpider, ListingSpider):
  name = 'individual_listing_spider'

  def __init__(self, *args, **kwargs):
    #hack process based utils expects id to be a primary key, but we're passing in a url
    #if we just passed in url, processbased utils would not forward it onto the crawler process

    url = kwargs['id']

    #get the root domain - but this is pretty naive. consider
    #https://github.com/john-kurkowski/tldextract
    netloc_split = urlparse(url).netloc.split(".")
    if 'www' in netloc_split:
      domain = netloc_split[1]
    else:
      domain = netloc_split[0]

    listing_sources = ListingSource.objects.filter(url__icontains=domain).all()
    source_dict = {k.url: k for k in listing_sources}

    closest_url = fuzzy_search.get_closest_word(url, source_dict.keys())

    config = source_dict[closest_url].scraper_config

    self.scraper = config.scraper
    self.scrape_url = url
    self.ref_object = config

    super(IndividualListingSpider, self).__init__(*args, **kwargs)
