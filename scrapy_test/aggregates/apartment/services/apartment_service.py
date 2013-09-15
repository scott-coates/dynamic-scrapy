from scrapy_test.aggregates.apartment import factories
from scrapy_test.aggregates.apartment.models import Apartment


def get_apartment(pk):
  return Apartment.objects.get(pk=pk)


def save_or_update(apartment):
  apartment.save(internal=True)


def adopt_listing(listing):
  try:
    apartment = Apartment.objects.find_from_listing(listing)
    apartment.adopt_listing(listing)
  except Apartment.DoesNotExist:
    apartment = factories.construct_apartment_from_listing(listing)

  save_or_update(apartment)

  return apartment

def update_availability(apartment):
  apartment.update_availability()
  save_or_update(apartment)

def notify_unavailable(apartment):
  apartment.notify_unavailable()
  save_or_update(apartment)
