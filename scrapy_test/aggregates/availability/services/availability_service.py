from scrapy_test.aggregates.availability.models import Availability


def save_or_update(availability):
  availability.aliases = availability.aliases.lower()
  availability.system_name = availability.system_name.lower()
  availability.save(internal=True)


def get_keyword_hash():
  availability_hash = {
    alias: availability.pk for availability in Availability.objects.all()
    for alias in availability.aliases.splitlines()
  }

  return availability_hash


def get_availability_from_str(availability_str):
  return None
