import pytest
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.tests.email_test_data import email_1


@pytest.mark.parametrize(("input_values", "expected"), [
  ({'spam_score': 2.3}, True),
  ({'spam_score': 4}, True),
  ({'spam_score': 1}, False),
  ({'something_else': 4}, False),
  ({'something_else': 4, 'spam_score': 6}, True),
])
def test_email_service_detects_spam(input_values, expected):
  assert expected == email_service.is_spam(**input_values)


def test_email_service_sets_direction():
  email = email_service.construct_email(**email_1)
  assert email.email_direction == Email.email_direction_incoming


def test_email_service_corrects_from_keyword():
  from_address = 'something@test.com'
  email = email_service.construct_email(**dict(email_1, **{'from': from_address}))
  assert email.from_address == from_address

def test_email_service_corrects_attachment():
  email_dict = dict(email_1, **{'attachments': 1})
  email_service.construct_email(**email_dict)
