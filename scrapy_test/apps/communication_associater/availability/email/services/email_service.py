import logging

from django.core.exceptions import ValidationError

from scrapy_test.apps.communication_associater.availability.email.constants import SEARCH_BODY_IDENTIFIER_RE
from scrapy_test.aggregates.result.models import Result

logger = logging.getLogger(__name__)


def request_availability_about_apartments(search, search_specific_email_message_request):
  results_to_request_notification = Result.objects.find_results_from_search(search)
  for r in results_to_request_notification:
    try:
      message = _get_availability_email_context(r)
    except:
      logger.exception("Error creating email message")
    else:
      pass


def _get_listing(result):
  #get the 'best' contact - the most recent contact w/ name + email
  listing = result.apartment.listings.exclude(is_deleted=True).order_by("-last_updated_date")[:1].get()
  return listing


def _get_address(result):
  address = result.apartment.address
  return address


def _get_availability_email_context(result):
  ret_val = {}

  listing = _get_listing(result)

  ret_val['address'] = _get_address(result)
  ret_val['bedroom_count'] = _get_bedroom_count(result)
  ret_val['price'] = _get_price(result)
  ret_val['signature'] = _get_signature(result)

  ret_val['contact'] = _get_contact_name(listing)
  ret_val['source'] = _get_source_name(listing)

  SearchSpecificEmailMessageRequest()


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


def _get_signature(result):
  return result.apartment.price


def validate_availability_email(message_body_template):
  if not SEARCH_BODY_IDENTIFIER_RE.search(message_body_template):
    raise ValidationError("body must contain identifier")


('{{ apartment.address1 }} Apartment',
 "Hi{% if apartment.contact_first_name %} {{ apartment.contact_first_name }}{% endif %},"
 "\n\nI saw your listing on {{ source }} for an apartment at {{ apartment.address1 }} ({% if apartment.bedroom %}{{ "
 "apartment.bedroom|floatformat }} BR{% else %}studio{% endif %} for ${{ apartment.price|floatformat:\"-2\" }}). I'm "
 "interested in this apartment. Is it still available? If so, when can I see it? Can you tell me anything else about "
 "the place?\n\nThanks,\n{{ signature }}\n"
