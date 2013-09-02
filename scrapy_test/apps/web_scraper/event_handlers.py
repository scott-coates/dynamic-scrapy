from django.dispatch import receiver
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.signals import sanitized, deleted
from scrapy_test.apps.web_scraper.services import web_scraper_tasks


@receiver(sanitized, sender=Listing)
def listing_sanitized_create_checker_callback(sender, **kwargs):
  web_scraper_tasks.add_listing_checker_task.delay(kwargs['instance'].id)


@receiver(deleted, sender=Listing)
def listing_deleted_remove_checker_callback(sender, **kwargs):
  web_scraper_tasks.delete_listing_checker_task.delay(kwargs['instance'].id)
