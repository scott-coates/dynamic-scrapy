from rest_framework import serializers
from rest_framework.relations import RelatedField
from scrapy_test.apps.domain.search.models import PotentialSearch


class PotentialSearchSerializer(serializers.ModelSerializer):
  search_aggregate = RelatedField()

  class Meta:
    model = PotentialSearch
    fields = ('id', 'search_attrs', 'purchased')
