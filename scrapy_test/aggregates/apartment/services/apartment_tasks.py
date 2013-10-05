from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.services import listing_service


@task
def adopt_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return apartment_service.adopt_listing(listing).id

@task
def update_availability_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  apartment = listing.apartment
  apartment_service.update_availability(apartment)

@task
def handle_result_notification_task(apartment_id, availability_type_system_name):
  apartment = apartment_service.get_apartment(apartment_id)
  apartment_service.handle_result_notification(apartment, availability_type_system_name)

