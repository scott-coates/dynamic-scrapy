import reversion
from scrapy_test.aggregates.amenity.models import Amenity

reversion.register(Amenity)
