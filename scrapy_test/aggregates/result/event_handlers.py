from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import became_unavailable
from scrapy_test.aggregates.result.services import result_tasks
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.signals import email_received


@receiver(email_received, sender=Email)
def email_received_occurred_callback(sender, **kwargs):
  #for now, we assume every email coming into the system is for the purposes of availability
  #if we ever add more reasons for incoming email, we'll need to address this.
  result_tasks.associate_incoming_email_with_result_task.delay(kwargs['instance'].id)

@receiver(became_unavailable, sender=Apartment)
def became_unavailable_callback(sender, **kwargs):
  reason = kwargs.pop('reason')
  result_tasks.notify_results_unavailable_task.delay(kwargs['instance'].id, reason)
