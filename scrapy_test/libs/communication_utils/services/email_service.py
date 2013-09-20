from django.conf import settings
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.signals import email_received


def is_spam(**kwargs):
  ret_val = False

  spam_score = kwargs.get('spam_score')

  try:

    spam_value = float(spam_score)

    if spam_value >= settings.SPAM_SCORE_THRESHOLD:
      ret_val = True

  except (ValueError, TypeError):
    pass

  return ret_val


def save_or_update(email):
  email.full_clean()
  email.save(internal=True)
  email_received.send(Email, instance=email)

  return email
