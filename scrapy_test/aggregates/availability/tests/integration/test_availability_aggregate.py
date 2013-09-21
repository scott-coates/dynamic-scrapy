import pytest
from scrapy_test.aggregates.availability.enums import AvailabilityStatusEnum
from scrapy_test.aggregates.availability.services import availability_service


@pytest.mark.django_db_with_migrations
@pytest.mark.parametrize(("availability_string", "expected_type"), [
  ("It's available. Not available, sorry", AvailabilityStatusEnum.Unavailable  ),
  ("It's available.", AvailabilityStatusEnum.Available  ),
])
def test_availability_uses_correct_type(availability_string, expected_type):
  availability_type = availability_service.get_availability_from_str(availability_string)
  assert expected_type == availability_type.system_name
