import pytest
from scrapy_test.aggregates.result.models import Result


@pytest.mark.parametrize(("apartment", "search", "expected_compliance_score"), [
  (None, None, None),
])
def test_result_calcs_compliance_score_correctly(apartment, search, expected_compliance_score):
  result = Result._from_apartment_and_search(apartment, search)
  assert result.compliance_score == expected_compliance_score
