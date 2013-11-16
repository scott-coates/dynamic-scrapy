from rest_framework import routers
from django.conf.urls import patterns, include, url
from scrapy_test.apps.rest_api.views.potential_search import PotentialSearchViewSet

# our consumer, in this case, restangular, doesn't conventionally append a '/' suffix, so it's just easier to disable
# the expectation on this side.
router = routers.DefaultRouter(trailing_slash=False)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
router.register('searchinit', PotentialSearchViewSet)

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
