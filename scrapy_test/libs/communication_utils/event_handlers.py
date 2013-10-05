from django.dispatch import receiver
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.signals import email_consumed_by_model


@receiver(email_consumed_by_model, sender=Email)
def email_consumed_by_model_callback(sender, **kwargs):
  email = kwargs['instance']
  associated_model = kwargs['associated_model']
  email_service.associate_model_with_email(email, associated_model)
