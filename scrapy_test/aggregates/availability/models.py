from django.db import models
from scrapy_test.aggregates.availability.managers import AvailabilityManager


class Availability(models.Model):
  objects = AvailabilityManager()

  name = models.CharField(max_length=128) #Is Available, Another user was notified unavailable
  system_name = models.CharField(max_length=128) #availabile, different_user_notified_unavailable
  aliases = models.TextField(blank=True, null=True)

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Availability, self).save(*args, **kwargs)
    else:
      from scrapy_test.aggregates.availability.services import availability_service

      availability_service.save_or_update(self)

  def __unicode__(self):
    return self.name
