import re
import logging

specific_phone_number_pattern = re.compile(
  r'(1[\W_]*)?(?P<whole>(?P<area_code>[2-9]\d{2})[\W_]*(?P<exchange>\d{3})[\W_]*(?P<number>\d{4}))'
)
vague_phone_number_pattern = re.compile(
  r'(1[\W_]*)?(?P<proto_phone_number>[2-9][\W_]*(?:\d[\W_]*){8}\d)'
)

logger = logging.getLogger(__name__)


def get_contact_name(contact_name_str):
  ret_val = None
  return ret_val


def get_contact_phone_number(phone_number_str):
  phone_number = None

  # Filter out potentially confounding artifacts in the text, like links.
  filtered_text = re.sub(r'https?://\S*', '--url--', phone_number_str)

  try:
    # Old way of finding phone numbers.
    old_phone_number_components = specific_phone_number_pattern.search(filtered_text)
    if old_phone_number_components:
      phone_number = u"({0}) {1}-{2}".format(old_phone_number_components.group('area_code'),
                                             old_phone_number_components.group('exchange'),
                                             old_phone_number_components.group('number'))
    else:
      # New way of finding phone numbers.
      new_phone_number_components = vague_phone_number_pattern.search(filtered_text)
      if new_phone_number_components:
        phone_number = u"({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(
          *(x for x in new_phone_number_components.group('proto_phone_number') if x.isalnum()))
  except:
    logger.warn("Error parsing phone number: {0}".format(phone_number_str), exc_info=1)

  return phone_number

