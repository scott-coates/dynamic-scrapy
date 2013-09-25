from django.core.exceptions import ValidationError
from mock import MagicMock
import pytest
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.apps.communication_associater.availability.email.services import email_service


@pytest.mark.parametrize(("input_contact_name", "expected_contact_name"), [
  (None, None),
])
def test_email_service_creates_contact_name(input_contact_name, expected_contact_name):
  mock_listing = MagicMock(spec=Listing)
  mock_listing.contact_name = input_contact_name
  assert expected_contact_name == email_service._get_contact_name(mock_listing)


def test_email_service_throws_error_when_missing_identifier():
  with pytest.raises(ValidationError):
    email_service.validate_availability_email('this is some body')