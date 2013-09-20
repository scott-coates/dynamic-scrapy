from scrapy_test.aggregates.availability.services import availability_service
from scrapy_test.aggregates.result import factories
from scrapy_test.aggregates.result.models import Result
from scrapy_test.libs.communication_utils.services import email_service


def create_result(apartment, listing):
  result = factories.construct_result(apartment, listing)

  save_or_update(result)

  return result


def get_result(pk):
  return Result.objects.get(pk=pk)


def save_or_update(result):
  result.save(internal=True)


def associate_incoming_email_with_result(email,
                                         _email_service=email_service,
                                         _availability_service=availability_service):
  #find the result tied to this email
  result = get_result(1)

  contents = _email_service.get_reply_contents(email)

  availability_type = _availability_service.get_availability_from_str(contents)
  #tie a result to this email

  result.add_availability_response(contents, email.sent_date, availability_type)

