from scrapy_test.aggregates.listing_source.models import ListingSource


def get_listing_source(pk):
  return ListingSource.objects.get(pk=pk)
