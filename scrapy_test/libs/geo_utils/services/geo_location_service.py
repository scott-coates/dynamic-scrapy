from scrapy_test.libs.geo_utils.sanitized_address import SanitizedAddress


def get_sanitized_address(lat, lng, address1, address2, city, state, zip_code):
  listing = {}
  return SanitizedAddress(listing.lat, listing.lng, listing.address1, listing.address2.listing.city, listing.state,
                          listing.zip_code)
