from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.result.services import result_service
from scrapy_test.libs.communication_utils.models import Email


@task
def associate_incoming_email_with_result_task(email_id):
  email = Email.objects.get(pk=email_id)

  return result_service.associate_incoming_email_with_result(email)


@task
def notify_results_unavailable_task(apartment_id, reason):
  apartment = apartment_service.get_apartment(apartment_id)

  return result_service.notify_results_unavailable(apartment, reason)
