from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.geo_utils.services import geo_location_service


def get_sanitized_address(address, city, state):
  try:
    existing_listing = Listing.objects.find_from_address(address, city, state)
    sanitized_listing = existing_listing
  except Listing.DoesNotExist:
    geocoded_listing = geo_location_service.get_geocoded_address(address, city, state)
    sanitized_listing = geocoded_listing

  return sanitized_listing
