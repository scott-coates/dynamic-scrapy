from django.db import models


class Amenity(models.Model):
  name = models.CharField(max_length=128)
  aliases = models.TextField(blank=True, null=True)

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Amenity, self).save(*args, **kwargs)
    else:
      from scrapy_test.aggregates.amenity.services import amenity_service

      amenity_service.save_or_update(self)


def __unicode__(self):
  return self.name
