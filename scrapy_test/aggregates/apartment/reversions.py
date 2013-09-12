import reversion
from scrapy_test.aggregates.apartment.models import Apartment, Amenity

reversion.register(Apartment, follow=['amenities'])
reversion.register(Amenity)
