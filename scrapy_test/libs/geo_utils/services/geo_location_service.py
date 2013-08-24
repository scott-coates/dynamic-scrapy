from scrapy_test.libs.geo_utils.geocoded_address import GeocodedAddress
from pygeocoder import Geocoder

_geocoder = Geocoder()


def _get_address_component(address_components, component):
  try:
    ret_val = next(x['short_name'] for x in address_components if component in x['types'])
  except StopIteration:
    ret_val = None

  return ret_val


def get_geocoded_address(address, city, state):
  address_format = "{0} {1} {2}".format(address, city, state)

  results = _geocoder.geocode(address_format)

  address_components = results.data[0]['address_components']

  address1 = _get_address_component(address_components, 'street_number')
  address2 = _get_address_component(address_components, 'subpremise')
  city = _get_address_component(address_components, 'sublocality')
  state = _get_address_component(address_components, 'administrative_area_level_1')
  zip_code = _get_address_component(address_components, 'postal_code')

  return GeocodedAddress(results.latitude, results.longitude, address1, address2, city, state,
                         zip_code, results.formatted_address)
