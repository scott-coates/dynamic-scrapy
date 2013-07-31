from scrapy_test.aggregates.listing_source.models import ListingSource


def get_listing_source(id):
  return ListingSource.objects.get(pk=id)
