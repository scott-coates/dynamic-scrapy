from collections import deque


class AggregateBase(object):
  def __init__(self):
    self._uncommitted_events = deque()

  def raise_event(self, event, sender, **named):
    self._uncommitted_events.append((event, sender, named))

  def send_events(self):
    while self._uncommitted_events:
      event_def = self._uncommitted_events.popleft()
      event_def[0].send(event_def[1], **event_def[2])
