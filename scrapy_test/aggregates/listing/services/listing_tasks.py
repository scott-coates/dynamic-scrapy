from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.services import listing_service


@task
def create_listing_task(**listing_attrs):
  return listing_service.create_listing(**listing_attrs).id

@task
def update_listing_task(**listing_attrs):
  return listing_service.update_listing(**listing_attrs).id

@task
def delete_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return listing_service.delete_listing(listing).id

@task
def associate_listing_with_apartment_task(listing_id, apartment_id):
  listing = listing_service.get_listing(listing_id)
  apartment = apartment_service.get_apartment(apartment_id)
  return listing_service.associate_listing_with_apartment(listing, apartment).id
