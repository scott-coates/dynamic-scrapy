import pytest
from scrapy_test.libs.text_utils.parsers import text_parser


@pytest.mark.parametrize(("input_values", "keywords", "expected"), [
  ('hi how are you', {'hi':1}, [1]),
  ('how are you', {'hi':1}, []),
  ('this foo bar is so dumb', {'foo bar':1}, [1]),
])
def test_text_parser_detects_correct_keywords(input_values, keywords, expected):
  assert expected == text_parser.get_canonical_name_from_keywords(input_values,keywords)
