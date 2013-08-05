from collections import deque


class AggregateBase(object):
  def __init__(self):
    self._uncommitted_events = deque()

  def _raise_event(self, event, sender, **kwargs):
    self._apply_event(event, sender, kwargs)
    self._uncommitted_events.append((event, sender, kwargs))

  def send_events(self):
    while self._uncommitted_events:
      event_def = self._uncommitted_events.popleft()
      event_def[0].send(self, event_def[1], **event_def[2])

  def _apply_event(self, event, sender, **kwargs):
    # the last element in the providing_args is used to re-created the name of the event later
    event_func_name = "_handle_{0}_event".format(event.providing_args[-1])

    handle_func = getattr(self, event_func_name, None)

    if not event_func_name: raise NotImplementedError("{0} must implement {1}".format(self.__class__.__name__,
                                                                                      event_func_name))

    handle_func(**kwargs)
