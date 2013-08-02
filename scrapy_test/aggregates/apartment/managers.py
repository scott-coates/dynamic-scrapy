from django.db import models


class ApartmentManager(models.Manager):
  def find_from_listing(self, listing):
    return self.filter(lat=listing.lat, lng=listing.lng, price=listing.price).get()
