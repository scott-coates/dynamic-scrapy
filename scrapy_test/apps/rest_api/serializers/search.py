from rest_framework import serializers
from scrapy_test.aggregates.search.models import Search
from scrapy_test.apps.domain.search.models import PotentialSearch


class SearchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Search

class PotentialSearchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PotentialSearch
    view_name = "search-init"
