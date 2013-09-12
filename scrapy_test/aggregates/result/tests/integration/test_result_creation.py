import pytest
from scrapy_test.aggregates.result.models import result
from scrapy_test.aggregates.result.services import result_service
from scrapy_test.aggregates.result.tests import result_test_data


@pytest.mark.django_db_with_migrations
def test_result_is_created_from_attrs():
  result_id = result_service.create_result(**result_test_data.result_1).id
  result = result.objects.get(pk=result_id)
  assert 1 == result.objects.count()
