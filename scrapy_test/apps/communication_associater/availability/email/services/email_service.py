import logging
from django.conf import settings

from django.core.exceptions import ValidationError
from django.template import Context, Template

from scrapy_test.apps.communication_associater.availability.email.constants import SEARCH_BODY_IDENTIFIER_RE
from scrapy_test.aggregates.result.models import Result
from scrapy_test.apps.communication_associater.availability.email.email_objects import \
  SearchSpecificEmailMessageInstance

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


def request_availability_about_apartments(search, search_specific_email_message_request):
  results_to_request_notification = Result.objects.find_results_from_search(search)
  for r in results_to_request_notification:
    try:
      message = _get_availability_email_message(r, search_specific_email_message_request)
    except:
      logger.exception("Error creating email message")
    else:
      pass


def _get_listing(result):
  #get the 'best' contact - the most recent contact w/ name + email
  listing = (
              result
              .apartment
              .listings
              .exclude(is_deleted=True)
              .exclude(contact_email_address=None)
              .order_by("-last_updated_date")
            )[:1].get()
  return listing


def _get_address(result):
  address = result.apartment.address
  return address


def _get_availability_email_message(result, search_specific_email_message_request):
  ret_val = {}

  listing = _get_listing(result)

  from_address = _get_from_email_address(search_specific_email_message_request)
  from_name = _get_from_name(search_specific_email_message_request)
  to_address = _get_to_email_address(listing)

  ret_val['address'] = _get_address(result)
  ret_val['bedroom_count'] = _get_bedroom_count(result)
  ret_val['price'] = _get_price(result)

  ret_val['signature'] = _get_signature(search_specific_email_message_request)
  ret_val['from_name'] = from_name
  ret_val['from_email_address'] = from_address

  ret_val['contact'] = _get_contact_name(listing)
  ret_val['source'] = _get_source_name(listing)
  ret_val['to_address'] = to_address
  context = Context(ret_val)

  subject_template = Template(search_specific_email_message_request.subject)
  subject = subject_template.render(context)

  body_template = Template(search_specific_email_message_request.body)
  body = body_template.render(context)

  return SearchSpecificEmailMessageInstance(from_address, from_name, subject, body, to_address)


def _get_contact_name(listing):
  contact_name = listing.contact_name
  if not contact_name:
    return None
  else:
    contact_name_parts = contact_name.strip().split()
    return contact_name.strip() if len(contact_name_parts) == 0 else contact_name_parts[0]


def _get_source_name(listing):
  return listing.listing_source.name


def _get_bedroom_count(result):
  return result.apartment.bedroom_count


def _get_price(result):
  return result.apartment.price


def _get_signature(search_specific_email_message_request):
  name = search_specific_email_message_request.from_name.split()[0]
  return name


def _get_from_name(search_specific_email_message_request):
  name = search_specific_email_message_request.from_name
  return name


def _get_from_email_address(search_specific_email_message_request):
  name = search_specific_email_message_request.from_name.replace(' ', '.')
  name = name + "@{0}".format(availability_from_email_address_domain)
  return name


def _get_to_email_address(listing):
  return listing.contact_email_address


def validate_availability_email(message_body_template):
  if not SEARCH_BODY_IDENTIFIER_RE.search(message_body_template):
    raise ValidationError("body must contain identifier")
