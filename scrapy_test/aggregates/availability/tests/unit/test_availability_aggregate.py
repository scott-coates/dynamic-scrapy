from mock import MagicMock
import pytest
from scrapy_test.aggregates.availability.enums import AvailabilityStatusEnum
from scrapy_test.aggregates.availability.services import availability_service


@pytest.mark.parametrize(("input_keyword_dict", "expected_type"), [
  (
    {'not available': AvailabilityStatusEnum.Unavailable, 'available': AvailabilityStatusEnum.Available},
    AvailabilityStatusEnum.Unavailable
  ),
])
def test_availability_uses_correct_type(input_keyword_dict, expected_type):
  text_parser_mock = MagicMock(get_canonical_name_from_keywords=MagicMock(return_value=input_keyword_dict))
  availability_service.get_availability_from_str("IGNORE ME", _text_parser=text_parser)
