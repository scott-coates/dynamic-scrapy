from django.db import models


class Availability(models.Model):
  name = models.CharField(max_length=128)
  aliases = models.TextField(blank=True, null=True)

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Availability, self).save(*args, **kwargs)
    else:
      from scrapy_test.aggregates.availability.services import availability_service

      availability_service.save_or_update(self)

  def __unicode__(self):
    return self.name
