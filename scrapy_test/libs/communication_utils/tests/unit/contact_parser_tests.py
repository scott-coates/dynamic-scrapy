import pytest
from scrapy_test.libs.communication_utils.parsing import contact_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('abc 555-555-5555 abc 123', '(555) 555-5555'),
])
def test_contact_parser_detects_phone_number(input_values, expected):
  assert expected == contact_parser.get_contact_phone_number(input_values)
