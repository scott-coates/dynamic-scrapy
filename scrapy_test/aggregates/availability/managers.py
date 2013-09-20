from django.db import models
from scrapy_test.aggregates.availability.enums import AvailabilityStatusEnum


class AvailabilityManager(models.Manager):
  def get_is_available_type(self):
    return self.get(system_name=AvailabilityStatusEnum.Available)

  def get_unavailable_type(self):
    return self.get(system_name=AvailabilityStatusEnum.Unavailable)

  def get_unknown_availability_type(self):
    return self.get(system_name=AvailabilityStatusEnum.UnknownAvailability)
