from scrapy_test.libs.common_domain.event_signal import EventSignal

created = EventSignal('created', __name__, 1, providing_args=['instance', 'attrs'])
initiated_availability_request = EventSignal('initiated_availability_request', __name__, 1, providing_args=['instance'])
