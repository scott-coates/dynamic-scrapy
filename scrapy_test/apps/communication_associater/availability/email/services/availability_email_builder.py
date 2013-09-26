import logging
from django.conf import settings

from django.template import Context, Template

from scrapy_test.apps.communication_associater.availability.email.email_objects import \
  SearchSpecificEmailMessageInstance

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


class AvailabilityEmailBuilder(object):
  def _get_listing(self):
    #get the 'best' contact - the most recent contact w/ name + email
    listing = (
                self
                .result
                .apartment
                .listings
                .exclude(is_deleted=True)
                .exclude(contact_email_address=None)
                .order_by("-last_updated_date")
              )[:1].get()
    return listing


  def _get_address(self):
    address = self.result.apartment.address
    return address


  def get_availability_email_message(self, result, search_specific_email_message_request):
    ret_val = {}

    self.result = result
    self.search_specific_email_message_request = search_specific_email_message_request
    self.listing = self._get_listing()

    from_address = self._get_from_email_address()
    from_name = self._get_from_name()
    to_address = self._get_to_email_address()

    ret_val['address'] = self._get_address()
    ret_val['bedroom_count'] = self._get_bedroom_count()
    ret_val['price'] = self._get_price()

    ret_val['signature'] = self._get_signature()
    ret_val['from_name'] = from_name
    ret_val['from_email_address'] = from_address

    ret_val['contact'] = self._get_contact_name()
    ret_val['source'] = self._get_source_name()
    ret_val['to_address'] = to_address
    context = Context(ret_val)

    subject_template = Template(self.search_specific_email_message_request.subject)
    subject = subject_template.render(context)

    body_template = Template(self.search_specific_email_message_request.body)
    body = body_template.render(context)

    return SearchSpecificEmailMessageInstance(from_address, from_name, subject, body, to_address)


  def _get_contact_name(self):
    contact_name = self.listing.contact_name
    if not contact_name:
      return None
    else:
      contact_name_parts = contact_name.strip().split()
      return contact_name.strip() if len(contact_name_parts) == 0 else contact_name_parts[0]


  def _get_source_name(self):
    return self.listing.listing_source.name


  def _get_bedroom_count(self):
    return self.result.apartment.bedroom_count


  def _get_price(self):
    return self.result.apartment.price


  def _get_signature(self):
    name = self.search_specific_email_message_request.from_name.split()[0]
    return name


  def _get_from_name(self):
    name = self.search_specific_email_message_request.from_name
    return name


  def _get_from_email_address(self):
    name = self.search_specific_email_message_request.from_name.replace(' ', '.')
    name = name + "@{0}".format(availability_from_email_address_domain)
    return name


  def _get_to_email_address(self):
    return self.listing.contact_email_address
