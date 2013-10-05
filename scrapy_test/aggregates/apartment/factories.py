from scrapy_test.aggregates.apartment.models import Apartment


def construct_apartment_from_listing(listing):
  apartment = Apartment._from_listing(listing)
  return apartment
