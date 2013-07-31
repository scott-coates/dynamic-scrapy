from scrapy_test.aggregates.listing.models import Listing


def get_listing(id):
  return Listing.objects.get(pk=id)

def create_listing(url, title, description, listing_source):
  listing = Listing(url=url, title=title, description=description, listing_source=listing_source)
  listing.save()
  return listing
