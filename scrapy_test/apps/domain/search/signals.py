from django.dispatch import Signal

potential_search_completed = Signal(providing_args=['instance'])
