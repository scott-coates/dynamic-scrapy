from rest_framework import viewsets
from scrapy_test.aggregates.search.models import Search
from scrapy_test.apps.rest_api.serializers.search import SearchSerializer


class SearchViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows searches to be viewed or edited.
  """
  queryset = Search.objects.all()
  serializer_class = SearchSerializer
