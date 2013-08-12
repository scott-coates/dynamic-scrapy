import pytest
from scrapy_test.libs.communication_utils.parsing import contact_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('abc 555-555-5555 abc 123', '(555) 555-5555'),
  ('Caliber Associates, Inc. (646) 597-6005', '(646) 597-6005'),
])
def test_contact_parser_detects_phone_number(input_values, expected):
  assert expected == contact_parser.get_contact_phone_number(input_values)

@pytest.mark.parametrize(("input_values", "expected"), [
  ('abc foo@bar.com abc 123', 'foo@bar.com'),
  ('Caliber Associates, Inc. foo@bar.com', 'foo@bar.com'),
  ('Caliber Associates, foo at bar dot com Inc. ', 'foo@bar.com'),
])
def test_contact_parser_detects_email_address(input_values, expected):
  assert expected == contact_parser.get_contact_email_address(input_values)
