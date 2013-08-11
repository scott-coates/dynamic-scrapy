import pytest
from scrapy_test.libs.geo_utils.parsing import address_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('123 fake st', True),
  ('5th', False),
])
def test_address_parser_detects_correct_street_addresses(input_values, expected):
  assert expected == address_parser.is_street_address(input_values)
