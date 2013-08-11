def is_street_address(address):
  address_split = [address_part for address_part in address.split() if address_part not in ("and", "at")]
  return len(address_split) >= 3


def is_cross_street_address(address):
  return " and " in address or " at " in address
