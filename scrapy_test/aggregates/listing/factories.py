from scrapy_test.aggregates.listing.models import Listing


def construct_listing(**kwargs):
  listing = Listing._from_attrs(**kwargs)
  return listing
