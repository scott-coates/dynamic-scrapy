import pytest
from scrapy_test.aggregates.listing.domain.listing_builder import ListingBuilder
from scrapy_test.aggregates.listing.tests.unit import listing_test_data

# region title
title_trimmed_at_beginning = listing_test_data.cl_listing_3952467416['title']
expected_title_trimmed_at_beginning = listing_test_data.cl_listing_3952467416_expected_title
# endregion


@pytest.mark.parametrize(("input_values", "expected"), [
  (title_trimmed_at_beginning, expected_title_trimmed_at_beginning),
])
def test_builder_title(input_values, expected):
  builder = ListingBuilder(title=input_values)
  builder._build_summary()
  assert builder.listing_attrs_output['title'] == expected
