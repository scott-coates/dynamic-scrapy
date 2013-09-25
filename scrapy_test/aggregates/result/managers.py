from datetime import timedelta
from django.db import models
from django.utils import timezone


class ResultManager(models.Manager):
  def find_results_to_be_notified_of_availability(self, apartment, ignore_availability_type=None):
    timespan = timezone.now() - timedelta(weeks=1)

    ret_val = self.filter(apartment=apartment, created_date__gte=timespan)

    if ignore_availability_type:
      ret_val = ret_val.exclude(availability_type=ignore_availability_type)

    return ret_val

  def find_results_from_search(self, search):
    return self.filter(search=search).exclude(apartment__is_available=False)
