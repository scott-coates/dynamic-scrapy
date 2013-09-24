from scrapy_test.aggregates.search import factories
from scrapy_test.aggregates.search.models import Search
from scrapy_test.libs.geo_utils.services import geo_location_service


def create_search(_geo_location_service=geo_location_service, **search_attrs):
  specified_location = search_attrs.get('specified_location', None)

  if not specified_location: raise TypeError('specified location is required')

  geocoded_address = _geo_location_service.get_geocoded_address(specified_location)

  search_attrs['address'] = geocoded_address.address1
  search_attrs['city'] = geocoded_address.city
  search_attrs['state'] = geocoded_address.state
  search_attrs['zip_code'] = geocoded_address.zip_code
  search_attrs['formatted_address'] = geocoded_address.formatted_address
  search_attrs['lat'] = geocoded_address.lat
  search_attrs['lng'] = geocoded_address.lng

  search = factories.construct_search(**search_attrs)

  save_or_update(search)

  return search


def save_or_update(search):
  search.save(internal=True)


def get_search(search_id):
  return Search.objects.get(pk=search_id)
