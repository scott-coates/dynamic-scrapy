from mock import MagicMock, call, ANY
import pytest
from scrapy_test.aggregates.amenity.services import amenity_service
from scrapy_test.aggregates.listing.domain import listing_builder
from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.services import listing_geo_service
from scrapy_test.aggregates.listing.tests import listing_test_data
from scrapy_test.libs.communication_utils.parsing import contact_parser
from scrapy_test.libs.datetime_utils.parsers import datetime_parser
from scrapy_test.libs.geo_utils.parsing import address_parser
from scrapy_test.libs.housing_utils.parsing import home_parser

# region title tests
from scrapy_test.libs.text_utils.parsers import text_parser

title_stripped = listing_test_data.cl_listing_3952467416_title
expected_title_stripped = listing_test_data.cl_listing_3952467416_expected_title

title_scalar = 'My Title'
expected_title_scalar = 'My Title'


@pytest.mark.parametrize(("input_values", "expected"), [
  (title_stripped, expected_title_stripped),
  (title_scalar, expected_title_scalar),
])
def test_builder_title_expected_actual(input_values, expected):
  builder = ListingBuilder(title=input_values)
  builder._build_title()
  assert builder.listing_attrs_output[listing_builder.TITLE] == expected


def test_builder_throws_appropriate_error_for_invalid_type():
  with pytest.raises(TypeError):
    builder = ListingBuilder(title=1)
    builder._build_title()

# endregion

# region description tests
def test_builder_description_combines_elements_into_scalar_description():
  builder = ListingBuilder(description=listing_test_data.cl_listing_3952467416_description)
  builder._build_description()
  description = builder.listing_attrs_output[listing_builder.DESCRIPTION]
  assert isinstance(description, basestring)


def test_builder_description_combines_elements_into_scalar_description():
  builder = ListingBuilder(description=listing_test_data.cl_listing_3952467416_description)
  builder._build_description()
  description = builder.listing_attrs_output[listing_builder.DESCRIPTION]
  assert description == listing_test_data.cl_listing_3952467416_expected_description

# endregion

# region date tests

def test_builder_uses_datetime_parser():
  datetime_parser_mock = MagicMock(spec=datetime_parser)

  datetime_parser_mock.get_datetime = MagicMock(
    return_value=listing_test_data.cl_listing_3952467416_posted_date
  )

  some_time = 'SOME TIME'

  builder = ListingBuilder(datetime_parser=datetime_parser_mock, posted_date=some_time)

  builder._build_posted_date()

  datetime_parser_mock.get_datetime.assert_called_with(some_time)


def test_builder_sets_posted_date_to_correct_date():
  datetime_parser_mock = MagicMock(spec=datetime_parser)

  datetime_parser_mock.get_datetime = MagicMock(
    return_value=listing_test_data.cl_listing_3952467416_posted_date
  )

  builder = ListingBuilder(datetime_parser=datetime_parser_mock, posted_date='IGNOREME')

  builder._build_posted_date()

  date = builder.listing_attrs_output[listing_builder.POSTED_DATE]

  return date


def test_builder_sets_last_updated_date_to_correct_date():
  datetime_parser_mock = MagicMock(spec=datetime_parser)

  datetime_parser_mock.get_datetime = MagicMock(
    return_value=listing_test_data.cl_listing_3952467416_last_updated_date
  )

  builder = ListingBuilder(datetime_parser=datetime_parser_mock, last_updated_date='IGNOREME')

  builder._build_last_updated_date()

  date = builder.listing_attrs_output[listing_builder.LAST_UPDATED_DATE]

  return date


  assert date == listing_test_data.cl_listing_3952467416_expected_last_updated_date

# endregion

#region url tests
def test_builder_gets_correct_url_from_list():
  url = 'http://newyork.craigslist.org/brk/abo/3981928312.html'

  builder = ListingBuilder(url=[url])

  builder._build_url()

  url_attr = builder.listing_attrs_output[listing_builder.URL]

  expected_url = url

  assert url_attr == expected_url

# endregion

# region address tests
def test_builder_sets_makes_address_distinct():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address=[address1, address1])
  builder._build_address()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS]
  assert isinstance(address_attr, basestring)


def test_builder_uses_firs_street_address_to_populate():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address=address1)
  builder._build_address()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS]
  assert address_attr is not None


def test_builder_uses_firs_cross_street_address_to_populate():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=False)
  address_parser_mock.is_cross_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address=address1)
  builder._build_address()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS]
  assert address_attr is not None


def test_builder_joins_addresses_if_no_valid_address():
  xstreet1 = 'Foo'
  xtreet2 = 'Bar'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=False)
  address_parser_mock.is_cross_street_address = MagicMock(return_value=False)
  builder = ListingBuilder(address_parser_mock, address=[xstreet1, xtreet2])
  builder._build_address()
  address_parser_mock.join_cross_street.assert_called_with({'Foo', 'Bar'})

# endregion

# region city tests
def test_builder_gets_correct_city_from_list():
  city = 'Brooklyn'

  builder = ListingBuilder(city=[city])

  builder._build_city()

  address_attr = builder.listing_attrs_output[listing_builder.CITY]

  assert address_attr == city

# endregion

# region state tests
def test_builder_gets_correct_city_from_list():
  state = 'NY'

  builder = ListingBuilder(state=[state])

  builder._build_state()

  address_attr = builder.listing_attrs_output[listing_builder.STATE]

  assert address_attr == state

# endregion

# region lat/lng tests
def test_builder_gets_correct_lat_lng_from_list():
  lat = '40.681449'
  lng = '-73.946437'

  builder = ListingBuilder(lat=[lat], lng=[lng])

  builder._build_lat_lng()

  lat_attr = builder.listing_attrs_output[listing_builder.LAT]
  lng_attr = builder.listing_attrs_output[listing_builder.LNG]

  lat_out = 40.681449
  lng_out = -73.946437

  assert lat_out == lat_attr
  assert lng_out == lng_attr

# endregion

# region formatted_address tests
def test_builder_uses_address_parser_if_formatted_address_present():
  address_parser_mock = MagicMock(spec=address_parser)
  builder = ListingBuilder(address_parser_mock, formatted_address='x')
  builder._build_formatted_address()
  address_parser_mock.parse_address.assert_called_with('x')

# endregion

#region address sanitization tests
def test_builder_delegates_address_sanitization():
  geo_service_mock = MagicMock(spec=listing_geo_service)

  builder = ListingBuilder(listing_geo_service=geo_service_mock)

  builder._sanitize_address()

  geo_service_mock.get_sanitized_address.assert_called_with(ANY, ANY, ANY)

#endregion

#region  bedroom tests
def test_builder_gets_correct_bedroom_from_list():
  bedroom_count = '2'

  builder = ListingBuilder(bedroom_count=[bedroom_count])

  builder._build_bedroom_count()

  bedroom_count_attr = builder.listing_attrs_output[listing_builder.BEDROOM_COUNT]

  expected_bedroom_count = 2

  assert bedroom_count_attr == expected_bedroom_count


def test_builder_gets_correct_bedroom_from_title_if_not_in_list():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_bedroom_count = 2
  home_parser_mock.get_bedroom_count = MagicMock(return_value=expected_bedroom_count)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_bedroom_count()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.BEDROOM_COUNT,
                                                                            expected_bedroom_count)


def test_builder_gets_correct_bedroom_even_if_0():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_bedroom_count = 0
  home_parser_mock.get_bedroom_count = MagicMock(return_value=expected_bedroom_count)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_bedroom_count()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.BEDROOM_COUNT,
                                                                            expected_bedroom_count)

# endregion

#region bathroom tests
def test_builder_gets_correct_bathroom_from_list():
  bathroom_count = '2'

  builder = ListingBuilder(bathroom_count=[bathroom_count])

  builder._build_bathroom_count()

  bedroom_count_attr = builder.listing_attrs_output[listing_builder.BATHROOM_COUNT]

  expected_bedroom_count = 2.0

  assert bedroom_count_attr == expected_bedroom_count


def test_builder_gets_correct_bathroom_from_title_if_not_in_list():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_bathroom_count = 2.0
  home_parser_mock.get_bathroom_count = MagicMock(return_value=expected_bathroom_count)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_bathroom_count()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.BATHROOM_COUNT,
                                                                            expected_bathroom_count)

def test_builder_gets_correct_bathroom_even_if_0():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_bathroom_count = 0
  home_parser_mock.get_bathroom_count = MagicMock(return_value=expected_bathroom_count)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_bathroom_count()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.BATHROOM_COUNT,
                                                                            expected_bathroom_count)

# endregion

#region sqfeet tests
def test_builder_gets_correct_sqfreet_from_list():
  sqfeet = '100'

  builder = ListingBuilder(sqfeet=[sqfeet])

  builder._build_sqfeet()

  sqfeet_attr = builder.listing_attrs_output[listing_builder.SQFEET]

  expected_sqfeet = 100.0

  assert sqfeet_attr == expected_sqfeet


def test_builder_gets_correct_bathroom_from_title_if_not_in_list():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_sqfeet = 100.0
  home_parser_mock.get_sqfeet = MagicMock(return_value=expected_sqfeet)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_sqfeet()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.SQFEET,
                                                                            expected_sqfeet)

# endregion

#region price tests
def test_builder_gets_correct_price_from_list():
  price = '100'

  builder = ListingBuilder(price=[price])

  builder._build_price()

  sqfeet_attr = builder.listing_attrs_output[listing_builder.PRICE]

  expected_price = 100.0

  assert sqfeet_attr == expected_price


def test_builder_gets_correct_price_title_if_not_in_list():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_price = 100.0
  home_parser_mock.get_price = MagicMock(return_value=expected_price)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_price()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.PRICE,
                                                                            expected_price)

# endregion

#region broker_fee tests
def test_builder_gets_correct_broker_fee_from_list():
  fee = 'True'

  builder = ListingBuilder(broker_fee=[fee])

  builder._build_broker_fee()

  broker_fee_attr = builder.listing_attrs_output[listing_builder.BROKER_FEE]

  expected_fee = True

  assert broker_fee_attr == expected_fee


def test_builder_gets_correct_broker_fee_from_url_if_not_in_list():
  home_parser_mock = MagicMock(spec=home_parser)

  expected_fee = True
  home_parser_mock.get_broker_fee_from_url = MagicMock(return_value=expected_fee)

  builder = ListingBuilder(home_parser=home_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_broker_fee()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.BROKER_FEE,
                                                                            expected_fee)

# endregion

#region contact name tests
def test_builder_uses_name_parser_when_in_name_provided():
  expected_name = 'foo bar'

  contact_parser_mock = MagicMock(spec=contact_parser)

  contact_parser_mock.get_contact_name = MagicMock(return_value=expected_name)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_name=[expected_name])

  builder._build_contact_name()

  contact_name = builder.listing_attrs_output[listing_builder.CONTACT_NAME]

  assert contact_name == expected_name


def test_builder_delegates_name_parsing_to_contact_parser():
  expected_name = 'foo bar'

  contact_parser_mock = MagicMock(spec=contact_parser)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_name=[expected_name])

  builder._build_contact_name()

  contact_parser_mock.get_contact_name.assert_called_with(expected_name)

# endregion

#region contact phone number tests
def test_builder_uses_phone_number_parser_when_in_name_provided():
  expected_phone_number = '555-555-5555'

  contact_parser_mock = MagicMock(spec=contact_parser)

  contact_parser_mock.get_contact_phone_number = MagicMock(return_value=expected_phone_number)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_phone_number=[expected_phone_number])

  builder._build_contact_phone_number()

  contact_phone_number = builder.listing_attrs_output[listing_builder.CONTACT_PHONE_NUMBER]

  assert contact_phone_number == expected_phone_number


def test_builder_delegates_phone_parsing_to_contact_parser():
  expected_phone_number = '555-555-5555'

  contact_parser_mock = MagicMock(spec=contact_parser)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_phone_number=[expected_phone_number])

  builder._build_contact_phone_number()

  contact_parser_mock.get_contact_phone_number.assert_called_with(expected_phone_number)


def test_builder_uses_description_for_phone_if_not_available():
  contact_parser_mock = MagicMock(spec=contact_parser)

  expected_phone = '(555) 555-5555'
  contact_parser_mock.get_contact_phone_number = MagicMock(return_value=expected_phone)

  builder = ListingBuilder(contact_parser=contact_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_contact_phone_number()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.CONTACT_PHONE_NUMBER,
                                                                            expected_phone)


# endregion

#region contact email tests
def test_builder_uses_email_parser_when_in_name_provided():
  expected_email = 'foo@bar.com'

  contact_parser_mock = MagicMock(spec=contact_parser)

  contact_parser_mock.get_contact_email_address = MagicMock(return_value=expected_email)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_email_address=[expected_email])

  builder._build_contact_email_address()

  contact_phone_number = builder.listing_attrs_output[listing_builder.CONTACT_EMAIL_ADDRESS]

  assert contact_phone_number == expected_email


def test_builder_delegates_email_parsing_to_contact_parser():
  expected_email_address = 'test@test.com'

  contact_parser_mock = MagicMock(spec=contact_parser)

  builder = ListingBuilder(contact_parser=contact_parser_mock, contact_email_address=[expected_email_address])

  builder._build_contact_email_address()

  contact_parser_mock.get_contact_email_address.assert_called_with(expected_email_address)


def test_builder_uses_description_for_email_if_not_available():
  contact_parser_mock = MagicMock(spec=contact_parser)

  expected_email = 'foo@bar.com'
  contact_parser_mock.get_contact_email_address = MagicMock(return_value=expected_email)

  builder = ListingBuilder(contact_parser=contact_parser_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = True

  builder._build_contact_email_address()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(listing_builder.CONTACT_EMAIL_ADDRESS,
                                                                            expected_email)


# endregion

#region amenity tests
def test_builder_gets_amenities_from_desc_if_not_in_list():
  amenity_service_mock = MagicMock(spec=amenity_service)

  builder = ListingBuilder(amenity_service=amenity_service_mock)

  builder.listing_attrs_output = MagicMock()
  builder.listing_attrs_output.get.return_value = 'IGNORE ME'
  builder._build_amenities()

  builder.listing_attrs_output.get.assert_called_with(listing_builder.DESCRIPTION)


def test_builder_delegates_amenitiy_lookup_to_parser():
  expected_amenities = [1, 2, 3]

  text_parser_mock = MagicMock(spec=text_parser)

  text_parser_mock.get_canonical_name_from_keywords = MagicMock(return_value=expected_amenities)

  amenity_service_mock = MagicMock(spec=amenity_service)

  builder = ListingBuilder(text_parser=text_parser_mock, amenity_service=amenity_service_mock)

  builder.listing_attrs_output = MagicMock()

  builder.listing_attrs_output.get.return_value = 'IGNORE ME'

  builder._build_amenities()

  assert builder.listing_attrs_output.__setitem__.call_args_list[0] == call(
    listing_builder.AMENITIES,
    expected_amenities
  )

#endregion
