from django.dispatch import Signal


class EventSignal(Signal):
  def __init__(self, name, version, providing_args=None):
    super(EventSignal, self).__init__(providing_args)
    self.name = name
    self.version = version
