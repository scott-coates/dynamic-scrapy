from scrapy_test.aggregates.amenity.models import Amenity


def save_or_update(amenity):
  amenity.aliases = amenity.aliases.lower()
  amenity.save(internal=True)

def get_keyword_hash():
  amenity_hash = {
    alias: amenity.pk for amenity in Amenity.objects.all()
    for alias in amenity.aliases.splitlines()
  }

  return amenity_hash
