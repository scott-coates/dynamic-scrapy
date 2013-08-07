from functools import partial
from django.test import SimpleTestCase
from mock import MagicMock
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase


class AggregateBaseTestCase(SimpleTestCase):
  class TestAggregate(AggregateBase):
    pass

  def test_aggregate_base_sends_event_in_order(self):
    results = []

    def side_effect(signal_num, *args):
      results.append(signal_num)

    aggregate_test = AggregateBaseTestCase.TestAggregate()

    signal1 = MagicMock()
    signal1.event_obj.send = MagicMock(side_effect=partial(side_effect,1))
    signal2 = MagicMock()
    signal2.event_obj.send = MagicMock(side_effect=partial(side_effect,2))

    aggregate_test._uncommitted_events.append(signal1)
    aggregate_test._uncommitted_events.append(signal2)

    aggregate_test.send_events()

    self.assertListEqual(results, [1, 2])
