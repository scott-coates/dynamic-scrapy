import re
import logging

bedroom_pattern = re.compile(r"(\d+)br", re.IGNORECASE)
bathroom_pattern = re.compile(r"([\d\.]+) bath", re.IGNORECASE)

logger = logging.getLogger(__name__)


def get_bedroom_count(bedroom_str):
  ret_val = None
  if 'studio' in bedroom_str:
    ret_val = 0
  else:
    match = bedroom_pattern.search(bedroom_str)
    if match:
      try:
        ret_val = int(match.groups()[0])
      except:
        logger.warn("Error casting bedroom count: {0}".format(bedroom_str), exc_info=1)
  return ret_val

def get_bathroom_count(bathroom_str):
  ret_val = None
  match = bathroom_pattern.search(bathroom_str)
  if match:
    try:
      ret_val = int(match.groups()[0])
    except:
      logger.warn("Error casting bathroom count: {0}".format(bathroom_str), exc_info=1)

  return ret_val
