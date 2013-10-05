from scrapy_test.libs.common_domain.event_signal import EventSignal

created_from_listing = EventSignal('created_from_listing', __name__, 1, providing_args=['instance', 'listing'])
adopted_listing = EventSignal('adopted_listing', __name__, 1, providing_args=['instance', 'listing'])
became_unavailable = EventSignal('became_unavailable', __name__, 1, providing_args=['instance', 'reason'])
