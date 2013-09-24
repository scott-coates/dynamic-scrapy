from scrapy_test.aggregates.apartment.enums import ApartmentUnavailableReasonEnum
from scrapy_test.aggregates.availability.models import Availability
from scrapy_test.aggregates.availability.services import availability_service
from scrapy_test.aggregates.result import factories
from scrapy_test.aggregates.result.models import Result
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.signals import email_consumed_by_model


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
  result = get_result(1)

  contents = _email_service.get_reply_contents(email)

  availability_type = _availability_service.get_availability_from_str(contents)

  result.add_availability_response(contents, email.sent_date, availability_type)

  save_or_update(result)

  email_consumed_by_model.send(Email, instance=_email_service, associated_model=result)


def notify_results_unavailable(apartment, reason):
  #find all results that are NOT `notified unavailable` because they've already been notified as unavailable. We
  # should set these to `other user found it to be unavailable`
  if reason == ApartmentUnavailableReasonEnum.NotifiedUnavailable:

    #we are going to exclude the `unavailable` type
    unavailable_type = Availability.objects.get_unavailable_type()

    different_user_notified_unavailable_type = Availability.objects.get_different_user_notified_unavailable_type()

    results = Result.objects.find_results_to_be_notified_of_availability(apartment, unavailable_type)
    for r in results:
      r.change_availability(different_user_notified_unavailable_type)
      save_or_update(r)

  elif reason == ApartmentUnavailableReasonEnum.AllListingsDeleted:
    all_listings_deleted_type = Availability.objects.get_all_listings_deleted_type()
    results = Result.objects.find_results_to_be_notified_of_availability(apartment)

    for r in results:
      r.change_availability(all_listings_deleted_type)
      save_or_update(r)
