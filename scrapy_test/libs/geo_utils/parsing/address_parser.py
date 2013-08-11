import re
address2_pattern = re.compile(r"((\#|apt|suite|ste)\.?\s?\d+)", re.IGNORECASE)

def is_street_address(address):
  address_split = [address_part for address_part in address.split() if address_part not in ("and", "at")]
  return len(address_split) >= 3


def is_cross_street_address(address):
  return " and " in address or " at " in address

def get_address2(address):
  ret_val = None

  match = address2_pattern.search(address)

  if match:
    ret_val = match.group()

  return ret_val
