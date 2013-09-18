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
  spam_score = models.FloatField()
  spam_report = models.TextField()

  email_direction_incoming = 1
  email_direction_outgoing = 2

  email_direction_choices = (
    (email_direction_incoming, 'Incoming'),
    (email_direction_outgoing, 'Outgoing'),
  )

  email_direction = models.PositiveSmallIntegerField(max_length=2, choices=email_direction_choices)
