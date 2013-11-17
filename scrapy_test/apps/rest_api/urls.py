from rest_framework import routers
from django.conf.urls import patterns, include, url
from scrapy_test.apps.rest_api.views.amenity import AmenityViewSet
from scrapy_test.apps.rest_api.views.potential_search import PotentialSearchViewSet

# our consumer, in this case, restangular, doesn't conventionally append a '/' suffix, so it's just easier to disable
# the expectation on this side.
router = routers.DefaultRouter(trailing_slash=False)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
router.register('potential_search', PotentialSearchViewSet)
router.register('amenity', AmenityViewSet)

potential_search_init = PotentialSearchViewSet.as_view({
  'get': 'resume_init',
  'post': 'create_init',
  'put': 'update_init',
})

potential_search_complete = PotentialSearchViewSet.as_view({
  'post': 'complete_init',
})

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^potential_search_init$', potential_search_init, name="potential_search_init"),
  url(r'^potential_search_complete$', potential_search_complete, name="potential_search_complete"),
  url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))
)
