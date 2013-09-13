import pytest
from scrapy_test.aggregates.apartment.models import Apartment
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
  result = Result._from_apartment_and_search(apartment, search)
  assert result.compliance_score == expected_compliance_score
