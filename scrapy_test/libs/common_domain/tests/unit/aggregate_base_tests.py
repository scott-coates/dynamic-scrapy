from django.test import SimpleTestCase
from mock import Mock
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase


class AggregateBaseTestCase(SimpleTestCase):

  def test_aggregate_base_sends_event_in_order(self):
    mock = Mock(spec=AggregateBase)
