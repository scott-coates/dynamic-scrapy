import textwrap
from django.core.exceptions import ValidationError
from mock import MagicMock
import pytest
from scrapy_test.apps.communication_associater.availability.email.services import email_service


def test_email_service_throws_error_when_missing_identifier():
  with pytest.raises(ValidationError):
    email_service.validate_availability_email('this is some body')


def test_email_service_gets_availability_identifier():
  text = textwrap.dedent("""\
  Hey this is some dude

  hope all is well

  res-id: 123

  Goodbye""")

  email = MagicMock(text=text)

  identifier = email_service.get_availability_identifier_from_email(email)

  assert '123' == identifier
