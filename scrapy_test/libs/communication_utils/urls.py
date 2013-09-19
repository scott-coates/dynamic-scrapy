from django.conf.urls import patterns, url

urlpatterns = patterns('scrapy_test.libs.communication_utils.views',
  url(r'^external/email/$', 'email_web_hook', name="email_web_hook"),
  url(r'^external/payment/$', 'payment_web_hook', name="payment_web_hook"),
)
