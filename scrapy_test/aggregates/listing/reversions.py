import reversion
from scrapy_test.aggregates.listing.models import Listing, Amenity

reversion.register(Listing, follow='amenities')
reversion.register(Amenity, follow='amenity_type')
