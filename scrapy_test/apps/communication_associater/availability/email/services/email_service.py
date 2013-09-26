import logging
from django.conf import settings

from django.core.exceptions import ValidationError

from scrapy_test.apps.communication_associater.availability.email.constants import EMAIL_AVAILABILITY_IDENTIFIER_RE
from scrapy_test.aggregates.result.models import Result
from scrapy_test.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder
from scrapy_test.libs.communication_utils.services import email_service

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


def request_availability_about_apartments(search, search_specific_email_message_request, _email_service=email_service):
  results_to_request_notification = Result.objects.find_results_from_search(search)

  email_builder = AvailabilityEmailBuilder()

  for r in results_to_request_notification:
    try:
      message = email_builder.get_availability_email_message(r, search_specific_email_message_request)
    except:
      logger.exception("Error creating email message")
    else:
      try:
        _email_service.send_email(
          message.from_address, message.from_name, message.to_address, message.subject, message.body, r
        )
      except:
        logger.exception("Error sending email message")


def validate_availability_email(message_body_template):
  if not EMAIL_AVAILABILITY_IDENTIFIER_RE.search(message_body_template):
    raise ValidationError("body must contain identifier")


def get_availability_identifier_from_email(email):
  match = EMAIL_AVAILABILITY_IDENTIFIER_RE.search(email.text)

  if not match:
    raise ValidationError("email text did not contain availability identifier")

  return match.groups(0)

