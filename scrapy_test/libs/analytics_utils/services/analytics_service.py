from mixpanel.tasks import EventTracker


def send_event(event_name, **kwargs):
  if not event_name: raise ValueError("event name is required")
  EventTracker.delay(event_name, **kwargs)

