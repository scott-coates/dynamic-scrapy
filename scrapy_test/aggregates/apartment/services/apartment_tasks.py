from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.services import listing_service


@task
def associate_listing_with_apartment_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return apartment_service.associate_listing_with_apartment(listing).id
