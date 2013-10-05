import pytest
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.aggregates.listing.tests import listing_test_data


@pytest.mark.django_db_with_migrations
def test_apartment_publishes_notified_unavailable():
  listing_id = listing_service.create_listing(**listing_test_data.cl_listing_4033538277).id
  listing = Listing.objects.get(pk=listing_id)
  apartment = listing.apartment
  apartment_service.notify_unavailable(apartment)

  assert apartment.is_available == False

  listings = Listing.objects.filter(apartment=apartment).values_list('is_deleted', flat=True)

  assert all(f == True for f in listings)
