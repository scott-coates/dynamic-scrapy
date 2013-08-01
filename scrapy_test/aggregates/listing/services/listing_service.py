from scrapy_test.aggregates.listing.factories import construct_listing
from scrapy_test.aggregates.listing.models import Listing


def get_listing(pk):
  return Listing.objects.get(pk=pk)


def create_listing(url, title, description, listing_source):
  listing = construct_listing(url, title, description, listing_source)
  save_or_update(listing)
  return listing


def save_or_update(listing):
  listing.save()
