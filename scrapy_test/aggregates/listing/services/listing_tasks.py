from celery.task import task
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.aggregates.listing_source.services import listing_source_service


@task
def create_listing_task(url, title, description, listing_source_id):
  listing_source = listing_source_service.get_listing_source(listing_source_id)
  return listing_service.create_listing(url, title, description, listing_source).id
