from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.services import listing_service


@task
def adopt_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return apartment_service.adopt_listing(listing).id
