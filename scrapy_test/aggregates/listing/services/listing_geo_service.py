from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.geo_utils.services import geo_location_service


def get_sanitized_address(lat, lng, address1, address2, city, state, zip_code):
  try:
    existing_listing = Listing.objects.find_from_address(lat, lng, address1, address2, city, state, zip_code)
  except:
    sanitized_listing = geo_location_service.get_sanitized_address(lat, lng, address1, address2, city, state, zip_code)
  else:
    sanitized_listing = existing_listing

  return sanitized_listing
