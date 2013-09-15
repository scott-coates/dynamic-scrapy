from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.enums import DeletedListingReasonEnum
from scrapy_test.aggregates.listing.signals import created, deleted
from scrapy_test.aggregates.listing.models import Listing


@receiver(created, sender=Listing)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.adopt_listing_task.delay(kwargs['instance'].id)


@receiver(deleted, sender=Listing)
def listing_deleted_callback(sender, **kwargs):
  reason = kwargs.pop('reason')

  if reason != DeletedListingReasonEnum.NotifiedUnavailable:
    apartment_tasks.update_availability_task.delay(kwargs['instance'].id)
