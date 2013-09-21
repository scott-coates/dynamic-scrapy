from email import message_from_string
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator

from jsonfield import JSONField
from django.db import models
from scrapy_test.libs.communication_utils.exceptions import EmailParseError
from scrapy_test.libs.datetime_utils.parsers import datetime_parser


class Email(models.Model):
  headers = models.TextField()
  text = models.TextField(blank=True, null=True)
  html = models.TextField(blank=True, null=True)
  to = models.TextField()
  from_address = models.TextField()
  cc = models.TextField(blank=True, null=True)
  subject = models.TextField(blank=True, null=True)
  dkim = JSONField()
  SPF = JSONField()
  envelope = JSONField()
  charsets = models.CharField(max_length=255)
  spam_score = models.FloatField(validators=[MaxValueValidator(settings.SPAM_SCORE_THRESHOLD)])
  spam_report = models.TextField()

  message_id = models.CharField(max_length=1024)
  in_reply_to_message_id = models.CharField(max_length=1024, blank=True, null=True)

  email_direction_incoming = 1
  email_direction_outgoing = 2
  email_direction_choices = (email_direction_incoming, 'Incoming'), (email_direction_outgoing, 'Outgoing')
  email_direction = models.PositiveSmallIntegerField(max_length=2, choices=email_direction_choices)

  sent_date = models.DateTimeField()

  content_type = models.ForeignKey(ContentType, blank=True, null=True)
  object_id = models.PositiveIntegerField(blank=True, null=True)
  content_object = generic.GenericForeignKey()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('message_id', 'sent_date')

  @classmethod
  def construct_incoming_email(cls, _datetime_parser=datetime_parser, **kwargs):
    kwargs['email_direction'] = Email.email_direction_incoming

    from_address = kwargs['from']
    kwargs['from_address'] = from_address

    del kwargs['from']
    del kwargs['attachments']

    ret_val = cls(**kwargs)

    message = message_from_string(ret_val.headers)
    message_dict = {t[0].lower(): t[1] for t in message.items()}

    #this field is not always required
    ret_val.in_reply_to_message_id = message_dict.get('in-reply-to')

    try:
      ret_val.message_id = message_dict['message-id']
      ret_val.sent_date = _datetime_parser.get_datetime(message_dict['date'])
    except KeyError:
      raise EmailParseError()

    return ret_val

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Email, self).save(*args, **kwargs)
    else:
      from scrapy_test.libs.communication_utils.services import email_service

      email_service.save_or_update(self)
