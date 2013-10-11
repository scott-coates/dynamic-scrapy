from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from scrapy_test.apps.domain.constants import POTENTIAL_SEARCH_SESSION_ID
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.services import potential_search_service
from scrapy_test.apps.rest_api.serializers.search import SearchSerializer, PotentialSearchSerializer


class SearchViewSet(viewsets.GenericViewSet):
  """
  API endpoint that allows searches to be viewed or edited.
  """
  def create(self, request, *args, **kwargs):
    pass

  @action()
  def init(self, request, pk=None):
    data = potential_search_service.get_search_attrs(request.DATA)

    potential_search = PotentialSearch(search_attrs=data)
    potential_search_service.save_or_update(potential_search)

    serializer = PotentialSearchSerializer(context={'request': request}, instance=potential_search)

    request.session[POTENTIAL_SEARCH_SESSION_ID] = potential_search.id

    return Response(
      serializer.data, status=status.HTTP_201_CREATED, headers=CreateModelMixin().get_success_headers(serializer.data)
    )
