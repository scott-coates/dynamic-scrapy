from functools import partial
from django.test import SimpleTestCase
from mock import MagicMock, create_autospec, ANY
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
    signal1.event_obj.send = MagicMock(side_effect=partial(side_effect, 1))
    signal2 = MagicMock()
    signal2.event_obj.send = MagicMock(side_effect=partial(side_effect, 2))

    aggregate_test._uncommitted_events.append(signal1)
    aggregate_test._uncommitted_events.append(signal2)

    aggregate_test.send_events()

    self.assertListEqual(results, [1, 2])

  def test_aggregate_uses_correct_naming_convention_when_applying(self):
    aggregate_test = AggregateBaseTestCase.TestAggregate()

    event = MagicMock()
    event.name = 'test'

    aggregate_test._handle_test_event = MagicMock()

    aggregate_test._apply_event(event)

    aggregate_test._handle_test_event.assert_called_with()
