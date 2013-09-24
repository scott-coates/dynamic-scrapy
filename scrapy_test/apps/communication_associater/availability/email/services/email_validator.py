from django.core.exceptions import ValidationError
from scrapy_test.apps.communication_associater.availability.email.constants import SEARCH_BODY_IDENTIFIER_RE


def validate_availability_email(message_body_template):
  if not SEARCH_BODY_IDENTIFIER_RE.search(message_body_template):
    raise ValidationError("body must contain identifier")
