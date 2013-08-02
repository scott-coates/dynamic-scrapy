from django.db import models
from scrapy_test.aggregates.apartment.models import Apartment


class ApartmentManager(models.Manager):
  def find_from_listing(self, listing):

    ret_val = None

    try:
      ret_val = self.filter(lat=listing.lat, lng=listing.lng, price=listing.price).order_by("-pk").get()
    except Apartment.DoesNotExist:
      pass

    return ret_val
