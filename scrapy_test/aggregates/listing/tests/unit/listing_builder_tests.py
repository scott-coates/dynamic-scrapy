import datetime
from mock import MagicMock, create_autospec
import pytest
from scrapy_test.aggregates.listing.domain import listing_builder
from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.tests.unit import listing_test_data

# region title tests
from scrapy_test.libs.geo_utils.parsing import address_parser

title_stripped = listing_test_data.cl_listing_3952467416['title']
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
  builder = ListingBuilder(description=listing_test_data.cl_listing_3952467416[listing_builder.DESCRIPTION])
  builder._build_description()
  description = builder.listing_attrs_output[listing_builder.DESCRIPTION]
  assert isinstance(description, basestring)


def test_builder_description_combines_elements_into_scalar_description():
  builder = ListingBuilder(description=listing_test_data.cl_listing_3952467416[listing_builder.DESCRIPTION])
  builder._build_description()
  description = builder.listing_attrs_output[listing_builder.DESCRIPTION]
  assert description == listing_test_data.cl_listing_3952467416_expected_description

# endregion

# region date tests
@pytest.fixture
def posted_date_3952467416():
  builder = ListingBuilder(posted_date=listing_test_data.cl_listing_3952467416[listing_builder.POSTED_DATE])
  builder._build_posted_date()
  date = builder.listing_attrs_output[listing_builder.POSTED_DATE]
  return date


@pytest.fixture
def last_updated_date_3952467416():
  builder = ListingBuilder(
    last_updated_date=listing_test_data.cl_listing_3952467416[listing_builder.LAST_UPDATED_DATE]
  )

  builder._build_last_updated_date()
  date = builder.listing_attrs_output[listing_builder.LAST_UPDATED_DATE]
  return date


def test_builder_sets_posted_date_to_date_type(posted_date_3952467416):
  assert isinstance(posted_date_3952467416, datetime.datetime)


def test_builder_sets_posted_date_to_correct_date(posted_date_3952467416):
  assert posted_date_3952467416 == listing_test_data.cl_listing_3952467416_expected_posted_date


def test_builder_sets_last_updated_date_to_correct_date(last_updated_date_3952467416):
  assert last_updated_date_3952467416 == listing_test_data.cl_listing_3952467416_expected_last_updated_date

# endregion

# region address1 tests
def test_builder_sets_makes_address_distinct():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address1=[address1, address1])
  builder._build_address1()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS1]
  assert isinstance(address_attr, basestring)


def test_builder_uses_firs_street_address_to_populate():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address1=address1)
  builder._build_address1()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS1]
  assert address_attr is not None


def test_builder_uses_firs_cross_street_address_to_populate():
  address1 = '123 test st'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=False)
  address_parser_mock.is_cross_street_address = MagicMock(return_value=True)
  builder = ListingBuilder(address_parser_mock, address1=address1)
  builder._build_address1()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS1]
  assert address_attr is not None


def test_builder_joins_addresses_if_no_valid_address():
  xstreet1 = 'Foo'
  xtreet2 = 'Bar'
  address_parser_mock = MagicMock(spec=address_parser)
  address_parser_mock.is_street_address = MagicMock(return_value=False)
  address_parser_mock.is_cross_street_address = MagicMock(return_value=False)
  builder = ListingBuilder(address_parser_mock, address1=[xstreet1, xtreet2])
  builder._build_address1()
  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS1]
  assert address_attr == 'Foo and Bar'

# endregion

# region address2 tests
def test_builder_uses_apt1_if_no_apt2():
  expected_address2 = 'apt. 5'

  address_parser_mock = MagicMock(spec=address_parser)

  builder = ListingBuilder(address_parser_mock, address2=None)

  address_parser_mock.get_address2 = MagicMock(return_value=expected_address2)

  builder.listing_attrs_output[listing_builder.ADDRESS1] = True #just mark it as not falsey

  builder._build_address2()

  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS2]

  assert address_attr == expected_address2

def test_builder_uses_apt2_if_available():
  address2 = 'apt. 5'

  builder = ListingBuilder(address2=[address2])

  builder._build_address2()

  address_attr = builder.listing_attrs_output[listing_builder.ADDRESS2]

  assert address_attr == address2
# endregion
