import logging
from django.core.exceptions import ValidationError
from scrapy_test.aggregates.result.models import Result
from scrapy_test.apps.communication_associater.availability.email.constants import SEARCH_BODY_IDENTIFIER_RE
from scrapy_test.apps.communication_associater.availability.email.search_specific_email_message import \
  SearchSpecificEmailMessage

logger = logging.getLogger(__name__)


def validate_availability_email(message_body_template):
  if not SEARCH_BODY_IDENTIFIER_RE.search(message_body_template):
    raise ValidationError("body must contain identifier")


def request_availability_about_apartments(search):
  results_to_request_notification = Result.objects.find_results_from_search(search)
  for r in results_to_request_notification:
    try:
      message = _get_availability_email_message(r)
    except:
      logger.exception("Error creating email message")
    else:
      pass


def _get_availability_email_message(result):
  SearchSpecificEmailMessage()


def _get_availability_contact_name(contact_name):
  if not contact_name:
    return None
  else:
    contact_name_parts = contact_name.strip().split()
    return contact_name.strip() if len(contact_name_parts) == 0 else contact_name_parts[0]

