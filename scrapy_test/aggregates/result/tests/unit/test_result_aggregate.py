from django.core.exceptions import ValidationError
import pytest
from scrapy_test.aggregates.result.models import result


@pytest.mark.parametrize(("min_value", "max_value", "result_attr"), [
  (3, 2, 'bedroom'),
  (3.5, 2.5, 'bathroom'),
  (1000, 850.50, 'sqfeet'),
  (3500, 2500.00, 'price'),
])
def test_result_throws_appropriate_error_for_invalid_max_settings(min_value, max_value, result_attr):
  result_attrs = {
    'description': 'My result',
    'specified_location': 'My Location',
    'geo_boundary_points': [{}, {}, {}],
    result_attr + "_min": min_value,
    result_attr + "_max": max_value,

  }

  with pytest.raises(ValidationError):
    result._from_attrs(**result_attrs)
