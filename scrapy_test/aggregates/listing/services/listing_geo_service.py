from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.value_objects import SanitizedAddress
from scrapy_test.libs.geo_utils.services import geo_location_service


def get_sanitized_address(address, city, state,
                          _listing_manager=Listing.objects, _geo_location_service=geo_location_service):
  try:
    existing_listing = _listing_manager.find_from_address(address, city, state)
    sanitized_listing = SanitizedAddress(existing_listing.lat,
                                         existing_listing.lng,
                                         existing_listing.address,
                                         existing_listing.city,
                                         existing_listing.state,
                                         existing_listing.zip_code,
                                         existing_listing.formatted_address)
  except Listing.DoesNotExist:
    geocoded_listing = _geo_location_service.get_geocoded_address(address, city, state)._asdict()

    formatted_parts = geocoded_listing['formatted_address'].split(',')

    address1 = geocoded_listing.pop('address1', None)
    if address1:
      #geo coding services won't return the cross street in the actual 'address' field. It'll only pull in the first
      # address like "5th st" when it should be "5th and 68th". The formatted address will contain this proper version
      geocoded_listing['address'] = formatted_parts[0]
    else:
      raise TypeError('address1 is required but was not returned from the geo location service')

    address2 = geocoded_listing.pop('address2', None)
    if address2:
      address2_formatted = ' #{0}'.format(address2)
      geocoded_listing['formatted_address'] = geocoded_listing['formatted_address'].replace(address2_formatted, '')

    sanitized_listing = SanitizedAddress(**geocoded_listing)
  return sanitized_listing
