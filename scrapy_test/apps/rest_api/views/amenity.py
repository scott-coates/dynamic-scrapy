from rest_framework import viewsets
from scrapy_test.aggregates.amenity.models import Amenity
from scrapy_test.apps.rest_api.serializers.amenity import AmenitySerializer


class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
  """
  API endpoint that allows potential searches to be retrieved or updated.
  """
  model = Amenity
  serializer_class = AmenitySerializer
  paginate_by = None
