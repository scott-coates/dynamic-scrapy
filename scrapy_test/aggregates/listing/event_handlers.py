from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import adopted_listing
from scrapy_test.aggregates.listing.services import listing_tasks


@receiver(adopted_listing, sender=Apartment)
def event_occurred_callback(sender, **kwargs):
  listing_tasks.associate_listing_with_apartment_task.delay(kwargs['listing'].id, kwargs['instance'].id)
