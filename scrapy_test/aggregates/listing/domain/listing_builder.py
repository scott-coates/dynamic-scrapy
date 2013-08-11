import collections
from scrapy_test.aggregates.listing import factories
from dateutil.parser import parse
from scrapy_test.libs.datetime_utils.timezone import time_zone_abbreviations
from scrapy_test.libs.geo_utils.parsing import address_parser

TITLE = 'title'
DESCRIPTION = 'description'
POSTED_DATE = 'posted_date'
LAST_UPDATED_DATE = 'last_updated_date'
ADDRESS1 = 'address1'

BEDROOM_COUNT = 'bedroom_count'
BATHROOM_COUNT = 'bathroom_count'
SQFEET = 'sqfeet'
PRICE = 'price'
BROKER_FEE = 'broker_fee'

newline_strip = '\r\n\t -'


class ListingBuilder(object):
  def __init__(self, _address_parser=address_parser, **listing_attrs):
    self.listing_attrs_input = listing_attrs
    self._address_parser = _address_parser
    self.listing_attrs_output = listing_attrs

  def _get_single_stripped_value(self, attr):
    if not isinstance(attr, basestring):
      try:
        attr = attr[0]
      except:
        raise TypeError("attr must be string or collection")
    attr = attr.strip(newline_strip)
    return attr

  #region summary
  def _build_title(self):
    title = self.listing_attrs_input.get(TITLE, None)
    if title:
      title = self._get_single_stripped_value(title)
      self._assign_output_attr(TITLE, title)

  def _build_description(self):
    description = self.listing_attrs_input.get(DESCRIPTION, None)
    if description:
      if isinstance(description, collections.Iterable):
        description = ''.join(description)
      description = description.strip(newline_strip)
      self._assign_output_attr(DESCRIPTION, description)


  def _build_posted_date(self):
    posted_date = self.listing_attrs_input.get(POSTED_DATE, None)

    if posted_date:
      posted_date = self._get_single_stripped_value(posted_date)

      try:
        posted_date = parse(posted_date, tzinfos=time_zone_abbreviations)
      except:
        raise Exception("invalid date: %s" % posted_date)

      self._assign_output_attr(POSTED_DATE, posted_date)

  def _build_last_updated_date(self):
    last_updated_date = self.listing_attrs_input.get(LAST_UPDATED_DATE, None)

    if last_updated_date:
      last_updated_date = self._get_single_stripped_value(last_updated_date)

      try:
        last_updated_date = parse(last_updated_date, tzinfos=time_zone_abbreviations)
      except:
        raise Exception("invalid date: %s" % last_updated_date)

      self._assign_output_attr(LAST_UPDATED_DATE, last_updated_date)

  #endregion

  #region address
  def _is_valid_address(self, address):
    return self._address_parser.is_street_address(address) or self._address_parser.is_cross_street_address(address)

  def _build_address1(self):
    address1 = self.listing_attrs_input.get(ADDRESS1, None)

    if address1:
      address1 = set(address1)

      for address in address1:
        if self._is_valid_address(address):
          self._assign_output_attr(ADDRESS1, address)
          break
      else:
        self._assign_output_attr(ADDRESS1, ' and '.join(address1))

    #endregion

  def _build_general_details(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

      #bath
      #sqfeet
      #price

  def _build_fees(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_location(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_contact_details(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_amenities(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def build_listing(self):
    self._build_title()
    self._build_description()
    self._build_general_details()
    self._build_fees()
    self._build_location()
    self._build_contact_details()
    self._build_amenities()

    return factories.construct_listing(**self.listing_attrs_output)

  def _assign_output_attr(self, key, value):
    self.listing_attrs_output[key] = value

