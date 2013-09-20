from django.dispatch import Signal

email_received = Signal(providing_args=['instance'])
