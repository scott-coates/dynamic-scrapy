from django.dispatch import Signal

sanitized = Signal(providing_args=['instance'])
deleted = Signal(providing_args=['instance'])
