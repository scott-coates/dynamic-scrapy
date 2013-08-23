from django.db import models
from django.db.models import Q


class ListingManager(models.Manager):
  def find_from_address(self, lat, lng, address1, address2, city, state, zip_code):
    return self.filter(
      Q(lat=lat, lng=lng)
      |
      Q(address1__iexact=address1, address2__iexact=address2, city__iexact=city, state__iexact=state, zip_code=zip_code)
    )[:1].get()
