from django.core.exceptions import ValidationError
import pytest
from scrapy_test.aggregates.search.models import Search


@pytest.mark.parametrize(("min_value", "max_value", "search_attr"), [
  (3, 2, 'bedroom'),
  (3.5, 2.5, 'bathroom'),
  (1000, 850.50, 'sqfeet'),
  (3500, 2500.00, 'price'),
])
def test_search_throws_appropriate_error_for_invalid_max_settings(min_value, max_value, search_attr):
  search_attrs = {
    'description': 'My Search',
    'specified_location': 'My Location',
    'geo_boundary_points': [{}, {}, {}],
    search_attr + "_min": min_value,
    search_attr + "_max": max_value,

  }

  with pytest.raises(ValidationError):
    Search._from_attrs(**search_attrs)


def test_search_throws_error_when_no_templates():
  search = Search()

  with pytest.raises(ValidationError):
    search.request_availability_from_contacts()


def test_search_throws_error_when_missing_identifier():
  search = Search(availability_email_subject_template='test subj',availability_email_body_template='test body')

  with pytest.raises(ValidationError):
    search.request_availability_from_contacts()
