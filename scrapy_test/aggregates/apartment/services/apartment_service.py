from scrapy_test.aggregates.apartment import factories
from scrapy_test.aggregates.apartment.models import Apartment


def get_apartment(pk):
  return Apartment.objects.get(pk=pk)


def save_or_update(apartment):
  apartment.save(internal=True)


def associate_listing_with_apartment(listing):
  try:
    apartment = Apartment.objects.find_from_listing(listing)
    apartment.adopt_listing(listing)
  except Apartment.DoesNotExist:
    apartment = factories.construct_apartment_from_listing(listing)

  save_or_update(apartment)

  return apartment

