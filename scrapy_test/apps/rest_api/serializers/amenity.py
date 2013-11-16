from rest_framework import serializers
from scrapy_test.aggregates.amenity.models import Amenity


class AmenitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Amenity
