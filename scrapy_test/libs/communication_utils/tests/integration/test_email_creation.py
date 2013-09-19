import pytest
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service
from scrapy_test.libs.communication_utils.tests.email_test_data import email_1


@pytest.mark.django_db_with_migrations
def test_email_is_created_from_attrs():
  email = Email.construct_incoming_email(**email_1)

  email_id = email_service.save_or_update(email).id

  email_aggregate = Email.objects.get(pk=email_id)

  assert 1 == Email.objects.count()

#   reply_message = '<20130916040724.5.38922.c45993@d4dab1f6-91ca-43a6-8ced-4d8a340e7403.prvt.dyno.rt.heroku.com>'
#   in_reply_to = 'In-Reply-To: %s\r\n' % reply_message
#
#   email = Email(**dict(email_dict, **{'headers': email_dict['headers'] + in_reply_to}))
#   assert email.in_reply_to_message_id == reply_message
#
#
# assert 1 == Listing.objects.count()
