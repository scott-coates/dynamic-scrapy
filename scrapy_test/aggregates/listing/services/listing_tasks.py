from celery.task import task
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.aggregates.listing_source.services import listing_source_service


@task
def create_listing_task(**listing_attrs):
  return listing_service.create_listing(**listing_attrs).id
