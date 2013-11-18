import logging
import sendgrid
from django.conf import settings

emailer = sendgrid.Sendgrid(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD, secure=True)

logger = logging.getLogger(__name__)


def send_email(from_address, from_name, to_address, subject, text, html):
  msg = sendgrid.Message((from_address, from_name), subject, text, html)
  msg.add_to(to_address)

  if settings.DEBUG:
    emailer.smtp.send(msg)
  else:
    logger.info(msg)
