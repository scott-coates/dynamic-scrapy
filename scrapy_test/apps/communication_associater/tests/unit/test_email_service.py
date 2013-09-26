from django.core.exceptions import ValidationError
import pytest
from scrapy_test.apps.communication_associater.availability.email.services import email_service

def test_email_service_throws_error_when_missing_identifier():
  with pytest.raises(ValidationError):
    email_service.validate_availability_email('this is some body')
