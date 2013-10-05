from django.dispatch import receiver
from scrapy_test.aggregates.apartment.enums import ApartmentUnavailableReasonEnum
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import adopted_listing, created_from_listing, became_unavailable
from scrapy_test.aggregates.listing.services import listing_tasks


@receiver(created_from_listing, sender=Apartment)
@receiver(adopted_listing, sender=Apartment)
def event_occurred_callback(sender, **kwargs):
  listing_tasks.associate_listing_with_apartment_task.delay(kwargs['listing'].id, kwargs['instance'].id)


@receiver(became_unavailable, sender=Apartment)
def became_unavailable_callback(sender, **kwargs):
  reason = kwargs.pop('reason')

  #if we were somehow notified externally that the apartment is no longer available, the listings should be updated.
  #but if we're simply marking the apartment as not available because all of the listings are dead,
  #we don't need to notify the listings again
  if reason != ApartmentUnavailableReasonEnum.AllListingsDeleted:
    listing_tasks.notify_listings_unavailable_task.delay(kwargs['instance'].id)
