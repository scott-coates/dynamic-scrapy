from scrapy_test.aggregates.result import factories
from scrapy_test.libs.geo_utils.services import geo_location_service


def create_result(_geo_location_service=geo_location_service, **result_attrs):
  specified_location = result_attrs.get('specified_location', None)

  if not specified_location: raise TypeError('specified location is required')

  geocoded_address = _geo_location_service.get_geocoded_address(specified_location)

  result_attrs['address'] = geocoded_address.address1
  result_attrs['city'] = geocoded_address.city
  result_attrs['state'] = geocoded_address.state
  result_attrs['zip_code'] = geocoded_address.zip_code
  result_attrs['formatted_address'] = geocoded_address.formatted_address
  result_attrs['lat'] = geocoded_address.lat
  result_attrs['lng'] = geocoded_address.lng

  result = factories.construct_result(**result_attrs)

  save_or_update(result)

  return result


def save_or_update(result):
  result.save(internal=True)
