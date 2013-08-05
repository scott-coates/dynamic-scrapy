from django.dispatch import receiver
from scrapy_test.aggregates.listing.event_sourcing import sanitized
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.apps.web_scraper.services import web_scraper_tasks


@receiver(sanitized, sender=Listing)
def listing_sanitized_create_checker_callback(sender, **kwargs):
  web_scraper_tasks.add_listing_checker_task.delay(kwargs['instance'].id)
