from scrapy_test.libs.common_domain.event_signal import EventSignal

adopted_listing = EventSignal('adopted_listing', __name__, 1, providing_args=['instance', 'listing'])
