from scrapy_test.aggregates.listing_source.models import ListingSource


def get_listing_source(pk):
  return ListingSource.objects.get(pk=pk)


def get_listing_source_by_name(listing_source_name):
  return ListingSource.objects.get(name=listing_source_name)
