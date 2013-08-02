from scrapy_test.aggregates.apartment.models import Apartment


def get_apartment(pk):
  return Apartment.objects.get(pk=pk)


def save_or_update(apartment):
  apartment.save(internal=True)
