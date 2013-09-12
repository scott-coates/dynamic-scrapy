from django.dispatch import receiver
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.signals import created, deleted, died
from scrapy_test.apps.web_scraper.services import web_scraper_tasks


@receiver(created, sender=Listing)
def listing_sanitized_create_checker_callback(sender, **kwargs):
  web_scraper_tasks.add_listing_checker_task.delay(kwargs['instance'].id)


@receiver(deleted, sender=Listing)
@receiver(died, sender=Listing)
def listing_remove_checker_callback(sender, **kwargs):
  web_scraper_tasks.delete_listing_checker_task.delay(kwargs['instance'].id)
