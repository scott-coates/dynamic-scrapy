from celery.task import task
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.communication_associater.availability.email.services import email_service


@task
def request_availability_about_apartments_task(search_id, search_specific_email_message_request):
  search = search_service.get_search(search_id)

  return email_service.request_availability_about_apartments(search, search_specific_email_message_request)
