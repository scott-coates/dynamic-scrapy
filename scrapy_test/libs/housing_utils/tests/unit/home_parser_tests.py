import pytest
from scrapy_test.libs.housing_utils.parsing import home_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('studio', 0),
  ('1br', 1),
])
def test_home_parser_detects_correct_bedroom_count(input_values, expected):
  assert expected == home_parser.get_bedroom_count(input_values)
