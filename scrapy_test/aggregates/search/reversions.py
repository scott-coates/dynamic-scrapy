import reversion
from scrapy_test.aggregates.search.models import Search, Amenity

reversion.register(Search, follow=['amenities'])
reversion.register(Amenity)
