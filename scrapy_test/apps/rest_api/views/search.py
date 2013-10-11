from django.forms.models import model_to_dict
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from scrapy_test.aggregates.search.models import Search
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.services import potential_search_service
from scrapy_test.apps.rest_api.serializers.search import SearchSerializer, PotentialSearchSerializer


class SearchViewSet(viewsets.GenericViewSet):
  """
  API endpoint that allows searches to be viewed or edited.
  """
  serializer_class = SearchSerializer

  def create(self, request, *args, **kwargs):
    pass


  @action()
  def init(self, request, pk=None):
    data = model_to_dict(Search(**request.DATA), fields=request.DATA.keys())

    potential_search = PotentialSearch(search_attrs=data)
    potential_search_service.save_or_update(potential_search)

    serializer = PotentialSearchSerializer(context={'request': request}, instance=potential_search)

    return Response(
      serializer.data, status=status.HTTP_201_CREATED, headers=CreateModelMixin().get_success_headers(serializer.data)
    )
