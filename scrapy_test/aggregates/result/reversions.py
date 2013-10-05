import reversion
from scrapy_test.aggregates.result.models import Result

reversion.register(Result)
