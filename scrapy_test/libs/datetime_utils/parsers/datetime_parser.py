from dateutil.parser import parse
from scrapy_test.libs.datetime_utils.timezone_abbreviations import time_zone_abbreviations


def get_datetime(datetime_str):
  return parse(datetime_str, tzinfos=time_zone_abbreviations)
