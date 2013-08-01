from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.models import Listing


def get_listing(pk):
  return Listing.objects.get(pk=pk)


def create_listing(**listing_attrs):
  builder = ListingBuilder(**listing_attrs)
  listing = builder.build_listing()
  save_or_update(listing)
  return listing


def save_or_update(listing):
  listing.save()
