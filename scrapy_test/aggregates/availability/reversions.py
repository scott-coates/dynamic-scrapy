import reversion
from scrapy_test.aggregates.availability.models import Availability

reversion.register(Availability)
