import reversion
from django.dispatch import Signal
from scrapy_test.aggregates.listing.models import Listing

reversion.register(Listing)

# the last element in the providing_args is used to re-created the name of the event later
created = Signal(providing_args=['instance', 'attrs', 'created'])
sanitized = Signal(providing_args=['instance', 'sanitized'])
deleted = Signal(providing_args=['instance', 'deleted'])
