from scrapy_test.libs.common_domain.event_signal import EventSignal

created_from_apartment_and_search = EventSignal(
  'created_from_apartment_and_search', __name__, 1, providing_args=['instance', 'apartment', 'search',
                                                                    'availability_type']
)

availability_contact_responded = EventSignal(
  'availability_contact_responded', __name__, 1,
  providing_args=['instance', 'response', 'response_date', 'availability_type']
)

availability_changed = EventSignal('availability_changed', __name__, 1,
                                   providing_args=['instance', 'availability_type'])
