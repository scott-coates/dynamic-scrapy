from django.dispatch import receiver
from scrapy_test.aggregates.listing.signals import listing_sanitized
from scrapy_test.apps.web_scraper.services import web_scraper_tasks


@receiver(listing_sanitized)
def listing_sanitized_create_checker_callback(sender, **kwargs):
  web_scraper_tasks.add_listing_checker_task.delay(sender.id)
