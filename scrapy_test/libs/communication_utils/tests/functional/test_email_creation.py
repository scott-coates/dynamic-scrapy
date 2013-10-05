from django.core.exceptions import ValidationError
import pytest
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.tests.email_test_data import email_1, email_3

@pytest.mark.django_db_with_migrations
def test_email_is_created_from_post(client):
  response = client.post('/communication/external/email/', email_3)
  assert 1 == Email.objects.count()

