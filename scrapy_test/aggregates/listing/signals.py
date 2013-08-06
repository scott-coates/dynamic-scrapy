from scrapy_test.libs.common_domain.event_signal import EventSignal

created = EventSignal('created', __name__, 1, providing_args=['instance', 'attrs'])
sanitized = EventSignal('sanitized', __name__, 1, providing_args=['instance'])
unsanitized = EventSignal('unsanitized', __name__, 1, providing_args=['instance', 'errors'])
deleted = EventSignal('deleted', __name__, 1, providing_args=['instance'])
