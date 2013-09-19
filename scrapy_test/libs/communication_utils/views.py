import logging
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from scrapy_test.libs.communication_utils.exceptions import EmailParseError
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.services import email_service

logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def email_web_hook(request):
  if request.GET.get('token') != settings.EXTERNAL_API_TOKEN and not settings.DEBUG:
    return HttpResponseForbidden()

  else:
    if not email_service.is_spam(**dict(request.POST.items())):

      try:
        email = Email.construct_incoming_email(**dict(request.POST.items()))
        email_service.save_or_update(email)

      except (EmailParseError, IntegrityError):
        logger.info('ignoring invalid email')
      except Exception:
        logger.exception('error accepting email')

        return HttpResponseServerError()
    else:
      logger.info('spam detected')

    return HttpResponse(status=200)
