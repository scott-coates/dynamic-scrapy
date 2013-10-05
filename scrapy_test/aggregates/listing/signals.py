from scrapy_test.libs.common_domain.event_signal import EventSignal

created = EventSignal('created', __name__, 1, providing_args=['instance', 'attrs'])

updated_last_updated_date = EventSignal('updated_last_updated_date', __name__, 1, providing_args=[
  'instance',
  'last_updated_date'
])

deleted = EventSignal('deleted', __name__, 1, providing_args=['instance', 'reason'])

associated_with_apartment = EventSignal('associated_with_apartment', __name__, 1, providing_args=['instance',
                                                                                                  'apartment'])
