from django.conf import settings
from django.core.validators import MaxValueValidator

from jsonfield import JSONField
from django.db import models


class Email(models.Model):
  headers = models.TextField()
  text = models.TextField(blank=True, null=True)
  html = models.TextField(blank=True, null=True)
  to = models.TextField()
  cc = models.TextField(blank=True, null=True)
  subject = models.TextField(blank=True, null=True)
  dkim = JSONField()
  SPF = JSONField()
  envelope = JSONField()
  charsets = models.CharField(max_length=255)
  spam_score = models.FloatField(validators=MaxValueValidator(settings.SPAM_SCORE_THRESHOLD))
  spam_report = models.TextField()

  message_id = models.CharField(max_length=1024)
  in_reply_to_message_id = models.CharField(max_length=1024, blank=True, null=True)

  email_direction_incoming = 1
  email_direction_outgoing = 2
  email_direction_choices = (email_direction_incoming, 'Incoming'), (email_direction_outgoing, 'Outgoing')
  email_direction = models.PositiveSmallIntegerField(max_length=2, choices=email_direction_choices)

  sent_date = models.DateTimeField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('message_id', 'sent_date')
