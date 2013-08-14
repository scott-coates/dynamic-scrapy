from scrapy_test.apps.web_scraper.spiders.individual_item_spider import IndividualItemSpider
from scrapy_test.apps.web_scraper.spiders.listing_spider import ListingSpider


class IndividualListingSpider(IndividualItemSpider, ListingSpider):
  name = 'individual_listing_spider'
