import datetime

from django.utils import timezone
from mock import MagicMock
import pytest
from django.utils.timezone import utc

from scrapy_test.aggregates.listing.tests.listing_test_data import eastern_time_zone
from scrapy_test.libs.datetime_utils.parsers import datetime_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('2013-08-07,  4:52PM EDT', eastern_time_zone.localize(datetime.datetime(2013, 8, 7, 16, 52))),
])
def test_datetime_parser_detects_correct_timezone(input_values, expected):
  assert expected == datetime_parser.get_datetime(input_values)


def test_datetime_parser_uses_relative_keywords():
  timezone_mock = MagicMock(spec=timezone)
  timezone_mock.now = MagicMock(return_value=datetime.datetime(2042, 1, 5, tzinfo=utc))

  expected = datetime.datetime(2042, 1, 1, tzinfo=utc)
  actual = datetime_parser.get_datetime('4 days on market', _datetime_service=timezone_mock)
  assert expected == actual
