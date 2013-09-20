from scrapy_test.aggregates.availability.enums import AvailabilityStatusEnum
from scrapy_test.aggregates.availability.models import Availability
from scrapy_test.libs.python_utils.collections import dict_utils
from scrapy_test.libs.text_utils.parsers import text_parser


def save_or_update(availability):
  availability.aliases = availability.aliases.lower()
  availability.system_name = availability.system_name.lower()
  availability.save(internal=True)


def get_keyword_hash():
  availability_hash = {
    alias: availability.system_name for availability in Availability.objects.all()
    for alias in availability.aliases.splitlines()
  }

  return availability_hash


def get_availability_from_str(availability_str, _text_parser=text_parser, _dict_utils=dict_utils):
  unavailable_type = Availability.objects.get_unavailable_type()
  is_available_type = Availability.objects.get_is_available_type()
  unknown_availability_type = Availability.objects.get_is_available_type()

  keyword_results = _text_parser.get_canonical_name_from_keywords(availability_str, get_keyword_hash())

  keyword_results = _dict_utils.invert_dict(keyword_results)

  if unavailable_type.system_name in keyword_results:
    return unavailable_type
  elif is_available_type.system_name in keyword_results:
    return is_available_type
  else:
    return unknown_availability_type
