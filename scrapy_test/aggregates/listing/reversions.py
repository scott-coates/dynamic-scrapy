import reversion
from scrapy_test.aggregates.listing.models import Listing

reversion.register(Listing)
