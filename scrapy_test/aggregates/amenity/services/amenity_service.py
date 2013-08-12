def save_or_update(amenity):
  amenity.aliases = amenity.aliases.lower()
  amenity.save(internal=True)
