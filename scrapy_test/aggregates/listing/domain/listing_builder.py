import os
from scrapy_test.aggregates.amenity.services import amenity_service
from scrapy_test.aggregates.listing import factories
from scrapy_test.aggregates.listing.services import listing_geo_service
from scrapy_test.aggregates.listing_source.services import listing_source_service
from scrapy_test.libs.communication_utils.parsing import contact_parser
from scrapy_test.libs.datetime_utils.parsers import datetime_parser
from scrapy_test.libs.geo_utils.parsing import address_parser
from scrapy_test.libs.housing_utils.parsing import home_parser
from scrapy_test.libs.text_utils.parsers import text_parser

LISTING_SOURCE_ID = 'listing_source_id'
LISTING_SOURCE = 'listing_source'

TITLE = 'title'
DESCRIPTION = 'description'
POSTED_DATE = 'posted_date'
LAST_UPDATED_DATE = 'last_updated_date'
URL = 'url'

ADDRESS = 'address'
CITY = 'city'
STATE = 'state'
ZIP_CODE = 'zip_code'
LAT = 'lat'
LNG = 'lng'
FORMATTED_ADDRESS = 'formatted_address'

BEDROOM_COUNT = 'bedroom_count'
BATHROOM_COUNT = 'bathroom_count'
SQFEET = 'sqfeet'
PRICE = 'price'
BROKER_FEE = 'broker_fee'

CONTACT_NAME = 'contact_name'
CONTACT_PHONE_NUMBER = 'contact_phone_number'
CONTACT_EMAIL_ADDRESS = 'contact_email_address'

AMENITIES = 'amenities'

_newline_strip = '\r\n\t -'


class ListingBuilder(object):
  def __init__(
      self,
      address_parser=address_parser,
      datetime_parser=datetime_parser,
      home_parser=home_parser,
      contact_parser=contact_parser,
      text_parser=text_parser,
      amenity_service=amenity_service,
      listing_geo_service=listing_geo_service,
      listing_source_service=listing_source_service,
      **listing_attrs
  ):
    self.listing_attrs_input = listing_attrs
    self._address_parser = address_parser
    self._datetime_parser = datetime_parser
    self._home_parser = home_parser
    self._contact_parser = contact_parser
    self._text_parser = text_parser
    self._amenity_service = amenity_service
    self._listing_geo_service = listing_geo_service
    self._listing_source_service = listing_source_service
    self.listing_attrs_output = {}

  def _get_single_stripped_value(self, attr, strip_chars=_newline_strip):
    if not isinstance(attr, basestring):
      try:
        attr = attr[0]
      except:
        raise TypeError("attr must be string or collection")
    attr = attr.strip(strip_chars)
    return attr

  #region listing source
  def _build_listing_source(self):
    listing_source_id = self.listing_attrs_input.get(LISTING_SOURCE_ID)
    listing_source = self._listing_source_service.get_listing_source(listing_source_id)
    self._assign_output_attr(LISTING_SOURCE, listing_source)

  #endregion

  #region summary
  def _build_title(self):
    title = self.listing_attrs_input.get(TITLE, None)
    if title:
      if not isinstance(title, basestring):
        title = ''.join(title)
      title = title.strip(_newline_strip)
      self._assign_output_attr(TITLE, title)

  def _build_description(self):
    description = self.listing_attrs_input.get(DESCRIPTION, None)
    if description:
      if not isinstance(description, basestring):
        description = (os.linesep + os.linesep).join(d.strip(_newline_strip) for d in description)
      description = description.strip(_newline_strip)
      self._assign_output_attr(DESCRIPTION, description)

  def _build_posted_date(self):
    posted_date = self.listing_attrs_input.get(POSTED_DATE, None)

    if posted_date:
      posted_date = self._get_single_stripped_value(posted_date)

      try:
        posted_date = self._datetime_parser.get_datetime(posted_date)
      except:
        raise Exception("invalid date: %s" % posted_date)

      self._assign_output_attr(POSTED_DATE, posted_date)

  def _build_last_updated_date(self):
    last_updated_date = self.listing_attrs_input.get(LAST_UPDATED_DATE, None)

    if last_updated_date:
      last_updated_date = self._get_single_stripped_value(last_updated_date)

      try:
        last_updated_date = self._datetime_parser.get_datetime(last_updated_date)
      except:
        raise Exception("invalid date: %s" % last_updated_date)

      posted_date = self.listing_attrs_output.get(POSTED_DATE, None)

      if posted_date and last_updated_date > posted_date:
        self._assign_output_attr(LAST_UPDATED_DATE, last_updated_date)

  def _build_url(self):
    url = self.listing_attrs_input.get(URL, None)

    if url:
      url = self._get_single_stripped_value(url)
      self._assign_output_attr(URL, url)

  #endregion

  #region address
  def _is_valid_address(self, address):
    return self._address_parser.is_street_address(address) or self._address_parser.is_cross_street_address(address)

  def _build_address(self):
    addresses = self.listing_attrs_input.get(ADDRESS, None)

    if addresses:
      addresses = set(addresses)

      for address in addresses:
        if self._is_valid_address(address):
          self._assign_output_attr(ADDRESS, address)
          break
      else:
        self._assign_output_attr(ADDRESS, self._address_parser.join_cross_street(addresses))

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

  def _build_lat_lng(self):
    lat = self.listing_attrs_input.get(LAT)
    lng = self.listing_attrs_input.get(LNG)

    if lat and lng:
      lat = self._get_single_stripped_value(lat, None)
      lng = self._get_single_stripped_value(lng, None)
      self._assign_output_attr(LAT, float(lat))
      self._assign_output_attr(LNG, float(lng))

  def _build_formatted_address(self):
    formatted_address = self.listing_attrs_input.get(FORMATTED_ADDRESS, None)

    if formatted_address:
      formatted_address = self._get_single_stripped_value(formatted_address)
      complete_address = self._address_parser.parse_address(formatted_address)

      self._assign_output_attr(ADDRESS, complete_address.address1)
      self._assign_output_attr(CITY, complete_address.city)
      self._assign_output_attr(STATE, complete_address.state)
      self._assign_output_attr(ZIP_CODE, complete_address.zip_code)
      self._assign_output_attr(FORMATTED_ADDRESS, complete_address.formatted_address)

  def _sanitize_address(self):
    listing_source = self.listing_attrs_output.get(LISTING_SOURCE)

    if not listing_source.trusted_geo_data:
      sanitized_address = self._listing_geo_service.get_sanitized_address(
        self.listing_attrs_output.get(ADDRESS),
        self.listing_attrs_output.get(CITY),
        self.listing_attrs_output.get(STATE),
      )

      self.listing_attrs_output[LAT] = sanitized_address.lat
      self.listing_attrs_output[LNG] = sanitized_address.lng
      self.listing_attrs_output[ADDRESS] = sanitized_address.address
      self.listing_attrs_output[CITY] = sanitized_address.city
      self.listing_attrs_output[STATE] = sanitized_address.state
      self.listing_attrs_output[ZIP_CODE] = sanitized_address.zip_code
      self.listing_attrs_output[FORMATTED_ADDRESS] = sanitized_address.formatted_address

  #endregion

  #region general
  def _build_bedroom_count(self):
    bedroom_count = self.listing_attrs_input.get(BEDROOM_COUNT)

    if bedroom_count:
      bedroom_count = self._get_single_stripped_value(bedroom_count)
      try:
        self._assign_output_attr(BEDROOM_COUNT, int(bedroom_count))
      except ValueError:
        bedroom_count = self.listing_attrs_input.get(BEDROOM_COUNT)
        if not isinstance(bedroom_count, basestring):
          bedroom_count = ''.join(bedroom_count)
        bedroom_count = self._home_parser.get_bedroom_count(bedroom_count)
        if bedroom_count is not None:
          self._assign_output_attr(BEDROOM_COUNT, bedroom_count)
    else:
      title = self.listing_attrs_output.get(TITLE)
      if title:
        bedroom_count = self._home_parser.get_bedroom_count(title)
        if bedroom_count is not None:
          self._assign_output_attr(BEDROOM_COUNT, bedroom_count)

  def _build_bathroom_count(self):
    bathroom_count = self.listing_attrs_input.get(BATHROOM_COUNT)

    if bathroom_count:
      bathroom_count = self._get_single_stripped_value(bathroom_count)
      try:
        self._assign_output_attr(BATHROOM_COUNT, float(bathroom_count))
      except ValueError:
        bathroom_count = self.listing_attrs_input.get(BATHROOM_COUNT)
        if not isinstance(bathroom_count, basestring):
          bathroom_count = ''.join(bathroom_count)
        bathroom_count = self._home_parser.get_bathroom_count(bathroom_count)
        if bathroom_count is not None:
          self._assign_output_attr(BATHROOM_COUNT, bathroom_count)
    else:
      title = self.listing_attrs_output.get(TITLE)
      if title:
        bathroom_count = self._home_parser.get_bathroom_count(title)
        if bathroom_count is not None:
          self._assign_output_attr(BATHROOM_COUNT, bathroom_count)

  def _build_sqfeet(self):
    sqfeet = self.listing_attrs_input.get(SQFEET)

    if sqfeet:
      sqfeet = self._get_single_stripped_value(sqfeet)
      try:
        self._assign_output_attr(SQFEET, float(sqfeet))
      except ValueError:
        sqfeet = self.listing_attrs_input.get(SQFEET)
        if not isinstance(sqfeet, basestring):
          sqfeet = ''.join(sqfeet)
        sqfeet = self._home_parser.get_sqfeet(sqfeet)
        if sqfeet is not None:
          self._assign_output_attr(SQFEET, sqfeet)
    else:
      title = self.listing_attrs_output.get(TITLE)
      if title:
        sqfeet = self._home_parser.get_sqfeet(title)
        if sqfeet:
          self._assign_output_attr(SQFEET, sqfeet)

  def _build_price(self):
    price = self.listing_attrs_input.get(PRICE)

    if price:
      price = self._get_single_stripped_value(price)
      try:
        self._assign_output_attr(PRICE, float(price))
      except ValueError:
        price = self.listing_attrs_input.get(PRICE)
        if not isinstance(price, basestring):
          price = ''.join(price)

        price = self._home_parser.get_price(price)
        if price:
          self._assign_output_attr(PRICE, price)
    else:
      title = self.listing_attrs_output.get(TITLE)
      if title:
        price = self._home_parser.get_price(title)
        if price:
          self._assign_output_attr(PRICE, price)

  def _build_broker_fee(self):
    broker_fee = self.listing_attrs_input.get(BROKER_FEE)

    if broker_fee:
      broker_fee = self._get_single_stripped_value(broker_fee)
      self._assign_output_attr(BROKER_FEE, broker_fee.lower() == 'true')
    else:
      url = self.listing_attrs_output.get(URL)
      if url:
        broker_fee = self._home_parser.get_broker_fee_from_url(url)
        if broker_fee:
          self._assign_output_attr(BROKER_FEE, broker_fee)

  #endregion

  #region contact
  def _build_contact_name(self):
    contact_name = self.listing_attrs_input.get(CONTACT_NAME)

    if contact_name:
      if not isinstance(contact_name, basestring):
        contact_name = ''.join(contact_name)
      contact_name = self._contact_parser.get_contact_name(contact_name)
      if contact_name:
        self._assign_output_attr(CONTACT_NAME, contact_name)

  def _build_contact_phone_number(self):
    contact_phone_number = self.listing_attrs_input.get(CONTACT_PHONE_NUMBER)

    if contact_phone_number:
      if not isinstance(contact_phone_number, basestring):
        contact_phone_number = ''.join(contact_phone_number)
      contact_phone_number = self._contact_parser.get_contact_phone_number(contact_phone_number)
      if contact_phone_number:
        self._assign_output_attr(CONTACT_PHONE_NUMBER, contact_phone_number)

    if not contact_phone_number:
      desc = self.listing_attrs_output.get(DESCRIPTION)
      if desc:
        contact_phone_number = self._contact_parser.get_contact_phone_number(desc)
        if contact_phone_number:
          self._assign_output_attr(CONTACT_PHONE_NUMBER, contact_phone_number)

  def _build_contact_email_address(self):
    contact_email_address = self.listing_attrs_input.get(CONTACT_EMAIL_ADDRESS)

    if contact_email_address:
      if not isinstance(contact_email_address, basestring):
        contact_email_address = ''.join(contact_email_address)
      contact_email_address = self._contact_parser.get_contact_email_address(contact_email_address)
      if contact_email_address:
        self._assign_output_attr(CONTACT_EMAIL_ADDRESS, contact_email_address)

    if not contact_email_address:
      desc = self.listing_attrs_output.get(DESCRIPTION)
      if desc:
        contact_email_address = self._contact_parser.get_contact_email_address(desc)
        if contact_email_address:
          self._assign_output_attr(CONTACT_EMAIL_ADDRESS, contact_email_address)

  #endregion

  #region amenities

  def _build_amenities(self):
    amenities = self.listing_attrs_input.get(AMENITIES)

    if not amenities:
      desc = self.listing_attrs_output.get(DESCRIPTION)
      if desc:
        amenities = desc

    if amenities:
      if not isinstance(amenities, basestring):
        amenities = ''.join(amenities)

      amenities = self._text_parser.get_canonical_name_from_keywords(
        amenities,
        self._amenity_service.get_keyword_hash()
      )

      if amenities:
        self._assign_output_attr(AMENITIES, amenities)

  #endregion

  def build_listing(self):
    self._build_listing_source()

    self._build_title()
    self._build_description()
    self._build_posted_date()
    self._build_last_updated_date()
    self._build_url()

    self._build_address()
    self._build_city()
    self._build_state()
    self._build_lat_lng()
    self._build_formatted_address()
    self._sanitize_address()

    self._build_bedroom_count()
    self._build_bathroom_count()
    self._build_sqfeet()
    self._build_price()
    self._build_broker_fee()

    self._build_contact_name()
    self._build_contact_phone_number()
    self._build_contact_email_address()

    self._build_amenities()

    return factories.construct_listing(**self.listing_attrs_output)

  def _assign_output_attr(self, key, value):
    self.listing_attrs_output[key] = value

