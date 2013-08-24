from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.geo_utils.services import geo_location_service


def get_sanitized_address(address, city, state):
  try:
    sanitized_listing = Listing.objects.find_from_address(address, city, state)
  except:
    sanitized_listing = geo_location_service.get_geocoded_address(address, city, state)

  return sanitized_listing
