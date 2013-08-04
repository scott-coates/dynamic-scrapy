from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.signals import listing_sanitized


@receiver(listing_sanitized)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.associate_listing_with_apartment_task.delay(sender.id)

