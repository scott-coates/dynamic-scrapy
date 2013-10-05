from django.contrib import admin
from django.conf.urls import patterns, include, url
from scrapy_test.libs.communication_utils import urls as communication_urls

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns(
  '',
  # Admin panel and documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^communication/', include(communication_urls)),
)
