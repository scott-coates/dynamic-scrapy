import textwrap

from django.utils import timezone
from mock import MagicMock
import pytest

from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.availability.models import Availability
from scrapy_test.aggregates.result.models import Result
from scrapy_test.aggregates.search.models import Search


@pytest.mark.parametrize(("apartment", "search", "expected_compliance_score"), [
  (Apartment(), Search(), 0),
  (Apartment(), Search(bedroom_min=2), 0),
  (Apartment(bedroom_count=2), Search(bedroom_min=2), 33),
  (
    Apartment(bedroom_count=2, bathroom_count=2, price=1000),
    Search(bedroom_min=1, bathroom_min=1, price_max=1200),
    100
  ),
])
def test_result_calcs_compliance_score_correctly(apartment, search, expected_compliance_score):
  availability_manager_mock = MagicMock(spec=Availability.objects)
  availability_manager_mock.get_unknown_availability_type.return_value = Availability()

  result = Result._from_apartment_and_search(apartment, search, _availability_manager=availability_manager_mock)
  assert result.compliance_score == expected_compliance_score


def test_result_appends_response_text():
  result = Result()
  result.add_availability_response('This is the oldest message', timezone.now(), Availability())
  result.add_availability_response('This is the newest message', timezone.now(), Availability())

  assert result.availability_contact_response == textwrap.dedent("""\
            This is the oldest message

            ==== Next Message ====

            This is the newest message""")
