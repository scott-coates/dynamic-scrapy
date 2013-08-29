# import pytest
# from scrapy_test.aggregates.listing.models import Listing
# from scrapy_test.aggregates.listing.services import listing_service
# from scrapy_test.aggregates.listing.tests import listing_test_data
# from scrapy_test.libs.django_utils.testing.utils import enable_south_migrations
#
# enable_south_migrations()
#
# @pytest.mark.django_db()
# def test_listing_is_created_from_attrs():
#   listing_service.create_listing(**listing_test_data.cl_listing_3952467416)
#   assert 1 == Listing.objects.count()
