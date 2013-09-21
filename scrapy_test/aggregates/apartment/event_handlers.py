from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.enums import DeletedListingReasonEnum
from scrapy_test.aggregates.listing.signals import created, deleted
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.result.models import Result
from scrapy_test.aggregates.result.signals import availability_contact_responded


@receiver(created, sender=Listing)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.adopt_listing_task.delay(kwargs['instance'].id)


@receiver(deleted, sender=Listing)
def listing_deleted_callback(sender, **kwargs):
  reason = kwargs.pop('reason')

  #if an apartment is notified as unavailable, we'll let the listings know they should be marked as such. In that
  # case, we don't need to re-notify the apartments that we've updated the listings,
  # because it was the apartment in the first place that let the listings know they needed to be updated.c
  if reason != DeletedListingReasonEnum.NotifiedUnavailable:
    apartment_tasks.update_availability_task.delay(kwargs['instance'].id)


@receiver(availability_contact_responded, sender=Result)
def result_contact_responded_callback(sender, **kwargs):
  result = kwargs['instance']
  apartment_tasks.check_notified_unavailable_task(result.apartment_id, result.availability_type.system_name)
