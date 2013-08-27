from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.signals import sanitized
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.libs.common_domain.event_signal import EventSignal


@receiver(sanitized,sender = Listing)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.associate_listing_with_apartment_task.delay(kwargs['instance'].id)

adopted_listing = EventSignal('adopted_listing', __name__, 1, providing_args=['instance', 'listing'])
