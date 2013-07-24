from scrapy.contrib.djangoitem import DjangoItem
from scrapy_test.aggregates.listing.models import Listing


class ListingScrapyItem(DjangoItem):
  django_model = Listing
