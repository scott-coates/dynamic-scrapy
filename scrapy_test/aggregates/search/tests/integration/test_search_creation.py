import pytest
from scrapy_test.aggregates.search.models import Search
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.aggregates.search.tests import search_test_data


@pytest.mark.django_db_with_migrations
def test_search_is_created_from_attrs():
  search_id = search_service.create_search(**search_test_data.search_1).id
  search = Search.objects.get(pk=search_id)
  assert 1 == Search.objects.count()
