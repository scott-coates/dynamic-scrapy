from scrapy_test.libs.communication_utils.signals import email_received


def is_spam(**kwargs):
  ret_val = False

  spam_score = kwargs.get('spam_score')

  try:

    spam_value = float(spam_score)

    if spam_value >= 2.3:
      ret_val = True

  except (ValueError, TypeError):
    pass

  return ret_val


def construct_email(**kwargs):
  spam_score = kwargs.get('spam_score')


def save_or_update(email):
  email.save()
  email_received.send(email)

  return None
