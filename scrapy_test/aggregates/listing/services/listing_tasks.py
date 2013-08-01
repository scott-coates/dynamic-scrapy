from celery.task import task
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.aggregates.listing_source.services import listing_source_service


@task
def create_listing_task(listing_source_id, **kwargs):
  listing_source = listing_source_service.get_listing_source(listing_source_id)
  return listing_service.create_listing(listing_source, **kwargs).id
