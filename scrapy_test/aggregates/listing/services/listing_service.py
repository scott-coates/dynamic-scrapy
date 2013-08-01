from scrapy_test.aggregates.listing.factories import construct_listing
from scrapy_test.aggregates.listing.models import Listing


def get_listing(pk):
  return Listing.objects.get(pk=pk)


def create_listing(listing_source, **kwargs):
  listing = None
  save_or_update(listing)
  return listing


def save_or_update(listing):
  listing.save()
