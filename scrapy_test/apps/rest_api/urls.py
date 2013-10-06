from rest_framework import routers
from django.conf.urls import patterns, include, url
from scrapy_test.apps.rest_api.views.search import SearchViewSet

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
router.register(r'search', SearchViewSet)

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
