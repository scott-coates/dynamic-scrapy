from celery.task import task
from scrapy_test.aggregates.listing.services import listing_service


@task
def create_listing_task(**listing_attrs):
  return listing_service.create_listing(**listing_attrs).id

@task
def update_listing_task(**listing_attrs):
  return listing_service.update_listing(**listing_attrs).id
