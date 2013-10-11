from rest_framework import routers
from django.conf.urls import patterns, include, url
from rest_framework.routers import Route
from scrapy_test.apps.rest_api.views.search import SearchViewSet

#our consumer, in this case, restangular, doesn't conventionally append a '/' suffix, so it's just easier to disable
# the expectation on this side.
router = routers.DefaultRouter(trailing_slash=False)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
router.register(r'search', SearchViewSet, 'search')

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^search/init/(?P<pk>[^/.]+)$', SearchViewSet.as_view({'put': 'update_init'}), name="search-init"),
  url(r'^search/init$', SearchViewSet.as_view(
    {
      'post': 'create_init',
      'get': 'resume_init',
      'put': 'update_init',
    }), name="search-init"),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
