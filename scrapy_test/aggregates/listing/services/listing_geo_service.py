from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.geo_utils.geocoded_address import GeocodedAddress
from scrapy_test.libs.geo_utils.services import geo_location_service


def get_sanitized_address(address, city, state,
                          _listing_manager=Listing.objects, _geo_location_service=geo_location_service):
  try:
    existing_listing = _listing_manager.find_from_address(address, city, state)
    sanitized_listing = GeocodedAddress(existing_listing.lat,
                                        existing_listing.lng,
                                        existing_listing.address,
                                        existing_listing.city,
                                        existing_listing.state,
                                        existing_listing.zip_code,
                                        existing_listing.formatted_address)
  except Listing.DoesNotExist:
    geocoded_listing = _geo_location_service.get_geocoded_address(address, city, state)._asdict()

    address2 = geocoded_listing.get('address2')
    if address2:
      address2_formatted = ' #{0}'.format(address2)
      geocoded_listing['formatted_address'] = geocoded_listing['formatted_address'].replace(address2_formatted, '')

    sanitized_listing = GeocodedAddress(**geocoded_listing)
  return sanitized_listing
