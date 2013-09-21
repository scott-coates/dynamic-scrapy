from datetime import timedelta
from django.db import models
from django.utils import timezone


class ResultManager(models.Manager):
  def find_results_to_be_notified_of_availability(self, apartment, excluded_availability_type):
    timespan = timezone.now() - timedelta(weeks=1)

    return (
      self.filter(apartment=apartment, created_date__gte=timespan)
      .exclude(availability_type=excluded_availability_type)
    )
