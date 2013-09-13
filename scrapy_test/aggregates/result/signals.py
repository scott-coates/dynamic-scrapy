from scrapy_test.libs.common_domain.event_signal import EventSignal

created_from_apartment_and_search = EventSignal(
  'created_from_apartment_and_search', __name__, 1, providing_args=['instance', 'apartment', 'search']
)
