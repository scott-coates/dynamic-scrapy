from scrapy.contrib.djangoitem import DjangoItem
from scrapy_test.aggregates.listing.models import Listing


class ListingItem(DjangoItem):
  django_model = Listing
