from scrapy_test.libs.geo_utils.sanitized_address import SanitizedAddress
from pygeocoder import Geocoder

def get_sanitized_address(lat, lng, address1, address2, city, state, zip_code):
  if lat and lng:
    results = Geocoder.reverse_geocode(lat,lng)
  return SanitizedAddress(listing.lat, listing.lng, listing.address1, listing.address2.listing.city, listing.state,
                          listing.zip_code)
