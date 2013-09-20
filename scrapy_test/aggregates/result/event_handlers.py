from django.dispatch import receiver
from scrapy_test.aggregates.result.services import result_tasks
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.signals import email_received


@receiver(email_received, sender=Email)
def email_received_occurred_callback(sender, **kwargs):
  result_tasks.associate_incoming_email_with_result.delay(kwargs['instance'].id)
