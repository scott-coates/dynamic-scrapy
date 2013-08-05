from scrapy_test.libs.common_domain.event_signal import EventSignal

created = EventSignal('created', 1, providing_args=['instance', 'attrs'])
sanitized = EventSignal('sanitized', 1, providing_args=['instance'])
unsanitized = EventSignal('unsanitzed', 1, providing_args=['instance', 'errors'])
deleted = EventSignal('deleted', 1, providing_args=['instance'])
