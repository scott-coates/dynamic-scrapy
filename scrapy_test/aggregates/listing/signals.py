from django.dispatch import Signal

listing_deleted = Signal(providing_args=[])


# @receiver(listing_deleted)
# def event_occurred_callback(sender, **kwargs):
#   pass
