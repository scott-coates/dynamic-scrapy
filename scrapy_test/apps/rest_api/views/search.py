from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from scrapy_test.aggregates.search.models import Search, PotentialSearch
from scrapy_test.aggregates.search.services import potential_search_service
from scrapy_test.apps.rest_api.serializers.search import SearchSerializer


class SearchViewSet(viewsets.GenericViewSet):
  """
  API endpoint that allows searches to be viewed or edited.
  """
  serializer_class = SearchSerializer

  def create(self, request, *args, **kwargs):
    pass


  @action()
  def init(self, request, pk=None):
    search = Search(**request.DATA)

    search_serializer = SearchSerializer(partial=True, context={'request': request}, instance=search)
    data = search_serializer.data

    potential_search = PotentialSearch(search_attrs=data)
    potential_search_service.save_or_update(potential_search)

    return Response(search_serializer.data, status=status.HTTP_201_CREATED,
                    headers={})
