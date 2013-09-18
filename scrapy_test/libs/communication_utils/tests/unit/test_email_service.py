from email.message import Message
import pytest
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

def test_email_service_constructs_email1():


  message = Message()

  email = email_service.construct_email(**email_1)
