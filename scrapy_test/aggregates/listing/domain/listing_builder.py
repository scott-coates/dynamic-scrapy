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
ADDRESS2 = 'address2'
CITY = 'city'
STATE = 'state'
ZIP_CODE = 'zip_code'
LAT = 'lat'
LNG = 'lng'

BEDROOM_COUNT = 'bedroom_count'
BATHROOM_COUNT = 'bathroom_count'
SQFEET = 'sqfeet'
PRICE = 'price'
BROKER_FEE = 'broker_fee'

_newline_strip = '\r\n\t -'


class ListingBuilder(object):
  def __init__(self, _address_parser=address_parser, **listing_attrs):
    self.listing_attrs_input = listing_attrs
    self._address_parser = _address_parser
    self.listing_attrs_output = listing_attrs

  def _get_single_stripped_value(self, attr, strip_chars=_newline_strip):
    if not isinstance(attr, basestring):
      try:
        attr = attr[0]
      except:
        raise TypeError("attr must be string or collection")
    attr = attr.strip(strip_chars)
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
      description = description.strip(_newline_strip)
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

  def _build_address2(self):
    address2 = self.listing_attrs_input.get(ADDRESS2)

    if address2:
      address2 = list(set(address2))[0]
    else:
      address2 = self.listing_attrs_output.get(ADDRESS1)
      if address2:
        address2 = self._address_parser.get_address2(address2)

    if address2:
      self._assign_output_attr(ADDRESS2, address2)

  def _build_city(self):
    city = self.listing_attrs_input.get(CITY)

    if city:
      city = self._get_single_stripped_value(city)
      self._assign_output_attr(CITY, city)

  def _build_state(self):
    state = self.listing_attrs_input.get(STATE)

    if state:
      state = self._get_single_stripped_value(state)
      self._assign_output_attr(STATE, state)

  def _build_zip_code(self):
    zip_code = self.listing_attrs_input.get(ZIP_CODE)

    if zip_code:
      zip_code = self._get_single_stripped_value(zip_code)
      self._assign_output_attr(ZIP_CODE, zip_code)

  def _build_lat_lng(self):
    lat = self.listing_attrs_input.get(LAT)
    lng = self.listing_attrs_input.get(LNG)

    if lat and lng:
      lat = self._get_single_stripped_value(lat, None)
      lng = self._get_single_stripped_value(lng, None)
      self._assign_output_attr(LAT, float(lat))
      self._assign_output_attr(LNG, float(lng))

  #endregion

  #region general
  def _build_bedroom_count(self):
    bedroom_count = self.listing_attrs_input.get(BEDROOM_COUNT)

    if bedroom_count:
      bedroom_count = self._get_single_stripped_value(bedroom_count)
      self._assign_output_attr(BEDROOM_COUNT, int(bedroom_count))

  #endregion


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
    self._build_bedroom_count()
    self._build_fees()
    self._build_location()
    self._build_contact_details()
    self._build_amenities()

    return factories.construct_listing(**self.listing_attrs_output)

  def _assign_output_attr(self, key, value):
    self.listing_attrs_output[key] = value

