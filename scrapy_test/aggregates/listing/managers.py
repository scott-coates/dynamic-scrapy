from django.db import models

class ListingManager(models.Manager):
  def find_from_address(self, address, city, state):
    return self.filter(address__iexact=address, city__iexact=city, state__iexact=state)[:1].get()
