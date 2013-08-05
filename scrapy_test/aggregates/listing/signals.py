from django.dispatch import Signal

sanitized = Signal(providing_args=['instance', 'event_name'])
deleted = Signal(providing_args=['instance', 'event_name'])
