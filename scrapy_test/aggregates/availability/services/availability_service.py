from scrapy_test.aggregates.availability.models import Availability
from scrapy_test.libs.text_utils.parsers import text_parser


def save_or_update(availability):
  availability.aliases = availability.aliases.lower()
  availability.system_name = availability.system_name.lower()
  availability.save(internal=True)


def get_keyword_hash():
  availability_hash = {
    alias: availability.pk for availability in Availability.objects.all()
    for alias in availability.aliases.splitlines()
  }

  return availability_hash


def get_availability_from_str(availability_str, _text_parser=text_parser):
  keyword_results = _text_parser.get_canonical_name_from_keywords(get_keyword_hash())
  return None
