from django.dispatch import receiver
from scrapy_test.aggregates.search.models import Search
from scrapy_test.aggregates.search.signals import initiated_availability_request
from scrapy_test.apps.communication_associater.availability.email.services import email_tasks


@receiver(initiated_availability_request, sender=Search)
def requested_availability_callback(sender, **kwargs):
  email_tasks.request_availability_about_apartments_task.delay(
    kwargs['instance'].id, kwargs['search_specific_email_message_request']
  )
