from mock import MagicMock, ANY
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.services import listing_geo_service
from scrapy_test.libs.geo_utils.geocoded_address import GeocodedAddress
from scrapy_test.libs.geo_utils.services import geo_location_service


def test_listing_geo_service_removes_address2():
  listing_manager_mock = MagicMock(spec=Listing.objects)
  listing_manager_mock.find_from_address.side_effect = Listing.DoesNotExist()

  geo_location_service_mock = MagicMock(spec=geo_location_service)
  geocoded_address = GeocodedAddress(ANY, ANY, ANY, '5a', ANY, ANY, ANY, '123 fake street #5a NY NY')

  geo_location_service_mock.get_geocoded_address = MagicMock(return_value=geocoded_address)

  sanitized_address = listing_geo_service.get_sanitized_address(ANY, ANY, ANY, listing_manager_mock,
                                                                geo_location_service_mock)

  assert sanitized_address.formatted_address == '123 fake street NY NY'
