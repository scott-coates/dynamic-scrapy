from django.utils import timezone
from mock import MagicMock
import pytest
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.tests.email_test_data import email_1


@pytest.fixture
def email_dict():
  email_dict = dict(email_1)

  del email_dict['attachments']
  del email_dict['from']

  return email_dict


def test_email_model_sets_message_id(email_dict):
  email = Email(**email_dict)
  assert email.message_id == '<11471247.33986.1361999987364.JavaMail.root@vms170015>'


def test_email_model_sets_date(email_dict):
  some_date = timezone.now()

  datetime_parser = MagicMock()
  datetime_parser.get_datetime = MagicMock(return_value=some_date)

  email = Email(_datetime_parser=datetime_parser, **email_dict)

  assert email.sent_date == some_date
