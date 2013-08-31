from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.aggregates.listing.tests import listing_test_data

#this line is required in order to use the db_with_migrations fixture
#http://pytest.org/latest/plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file
pytest_plugins = "scrapy_test.libs.django_utils.testing.utils"

def test_listing_is_created_from_attrs(db_with_migrations):
  listing = listing_service.create_listing(**listing_test_data.cl_listing_4033538277)
  assert 1 == Listing.objects.count()
