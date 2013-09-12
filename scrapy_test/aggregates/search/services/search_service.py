from scrapy_test.aggregates.search import factories
from scrapy_test.libs.geo_utils.services import geo_location_service


def create_search(_geo_location_service=geo_location_service, **search_attrs):
  search = factories.construct_apartment_from_listing(**search_attrs)

  return search


def save_or_update(search):
  search.save(internal=True)
