import re
address2_pattern = re.compile(r"((\#|apt|suite|ste)\.?\s?\d+)")

def get_bedroom_count(bedroom_str):
  ret_val = None
  if 'studio' in bedroom_str:
    ret_val = 0
  return ret_val
