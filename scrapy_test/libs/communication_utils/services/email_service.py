from scrapy_test.libs.communication_utils.signals import email_received


def is_spam(**kwargs):
  spam_score = kwargs.get('spam_score')


def construct_email(**kwargs):
  spam_score = kwargs.get('spam_score')


def save_or_update(email):
  email_received.send(email)
  email.save(internal=True)

  return None
