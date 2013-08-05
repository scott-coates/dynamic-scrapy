from django.dispatch import Signal

# the last element in the providing_args is used to re-created the name of the event later
# the second-to-last element in the providing_args is used to provide the version
created = Signal(providing_args=['instance', 'attrs', 1, 'created'])
sanitized = Signal(providing_args=['instance', 1, 'sanitized'])
deleted = Signal(providing_args=['instance', 1, 'deleted'])
