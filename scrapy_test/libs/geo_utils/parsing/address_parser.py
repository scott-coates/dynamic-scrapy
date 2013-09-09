import re

address2_pattern = re.compile(r"((\#|apt|suite|ste)\.?\s?\d+)", re.IGNORECASE)
zip_code_pattern = re.compile(r'^\d{5}(?:-\d{4})?$')
well_formatted_pattern = re.compile(
  r'(?:(?P<building_name>[\w\s\-]+) at )?'
  r'(?P<address_number>[\d\-]+)'
  r'(?P<street>[\w\s\-]+(?=\s+in))'
  r'(?: in (?P<neighborhood>[\w\s\-]+))?,'
  r'(?P<city>[\w\s\-]+),'
  r'(?P<state>\w{2})'
  r'(?P<zip>\d{5})')

def is_street_address(address):
  address_split = [address_part for address_part in address.split() if address_part not in ("and", "at")]
  return len(address_split) >= 3 and address_split[0].isdigit()


def is_cross_street_address(address):
  return " and " in address or " at " in address or " & " in address


def join_cross_street(address):
  return ' & '.join(address)


def is_valid_zip_code(zip_code):
  return bool(zip_code_pattern.search(zip_code))


def get_address2(address):
  ret_val = None

  match = address2_pattern.search(address)

  if match:
    ret_val = match.group()

  return ret_val
