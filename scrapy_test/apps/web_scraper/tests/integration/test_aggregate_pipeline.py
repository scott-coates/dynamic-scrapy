import pytest
from scrapy_test.aggregates.listing_source.models import ListingSource
from scrapy_test.libs.django_utils.testing.utils import enable_south_migrations

enable_south_migrations()

@pytest.mark.django_db()
def test_aggregate_pipeline_creates_listing():
  x = ListingSource.objects.count()
  assert x != 0
