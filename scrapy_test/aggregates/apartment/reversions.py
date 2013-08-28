import reversion
from scrapy_test.aggregates.apartment.models import Apartment

reversion.register(Apartment, follow=['amenities'])
