bedroom_count = 'bedroom_count'


class ListingBuilder(object):
  def __init__(self, **kwargs):
    self.listing_attrs_input = kwargs
    self.listing_attrs_output = kwargs
    pass

  def _build_bedroom_count(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

  def build_listing(self):
    self._build_bedroom_count()

    return 'foo'
