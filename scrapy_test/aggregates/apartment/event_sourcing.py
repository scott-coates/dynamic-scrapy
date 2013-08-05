from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.event_sourcing import sanitized
from scrapy_test.aggregates.listing.models import Listing


@receiver(sanitized,sender = Listing)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.associate_listing_with_apartment_task.delay(kwargs['instance'].id)

