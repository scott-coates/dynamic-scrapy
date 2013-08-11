import pytest
from scrapy_test.libs.geo_utils.parsing import address_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('123 fake st', True),
  ('100 e 55th', True),
  ('5th', False),
  ('5th and 55th', False),
])
def test_address_parser_detects_correct_street_addresses(input_values, expected):
  assert expected == address_parser.is_street_address(input_values)

@pytest.mark.parametrize(("input_values", "expected"), [
  ('62nd at york', True),
  ('21 and broadway', True),
  ('67 w 58th', False),
  ('250 e66', False),
])
def test_address_parser_detects_correct_cross_street_addresses(input_values, expected):
  assert expected == address_parser.is_cross_street_address(input_values)
