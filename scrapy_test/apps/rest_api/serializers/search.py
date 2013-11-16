from rest_framework import serializers
from scrapy_test.aggregates.search.models import Search


class SearchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Search
