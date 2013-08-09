import pytest
from scrapy_test.aggregates.listing.domain import listing_builder
from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.tests.unit import listing_test_data

# region title tests
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
# endregion
