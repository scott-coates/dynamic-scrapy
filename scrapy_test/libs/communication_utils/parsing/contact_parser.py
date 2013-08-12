import re
import logging

phone_number_pattern = re.compile(r"(\d+)br", re.IGNORECASE)

logger = logging.getLogger(__name__)


def get_contact_name(contact_name_str):
  ret_val = None
  return ret_val

def get_phone_number(phone_number_str):
  ret_val = None
  match = phone_number_pattern.search(phone_number_str)
  if match:
    ret_val = int(match.groups()[0])
  return ret_val
