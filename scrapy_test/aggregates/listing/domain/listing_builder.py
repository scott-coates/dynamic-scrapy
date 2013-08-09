import collections
from scrapy_test.aggregates.listing import factories

BEDROOM_COUNT = 'bedroom_count'
BATHROOM_COUNT = 'bathroom_count'
SQFEET = 'sqfeet'
PRICE = 'price'
BROKER_FEE = 'broker_fee'
TITLE = 'title'
DESCRIPTION = 'description'
newline_strip = '\r\n\t -'


class ListingBuilder(object):
  def __init__(self, **listing_attrs):
    self.listing_attrs_input = listing_attrs
    self.listing_attrs_output = listing_attrs

  def _build_title(self):
    title = self.listing_attrs_input.get(TITLE, None)
    if title:
      if not isinstance(title, basestring):
        try:
          title = title[0]
        except:
          raise TypeError("title must be string or collection")
      title = title.strip(newline_strip)
      self._assign_output_attr(TITLE, title)

  def _build_description(self):
    description = self.listing_attrs_input.get(DESCRIPTION, None)
    if description:
      if isinstance(description, collections.Iterable):
        description = ''.join(description)
      description = description.strip(newline_strip)
      self._assign_output_attr(DESCRIPTION, description)

  def _build_general_details(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

      #bath
      #sqfeet
      #price

  def _build_fees(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_location(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_contact_details(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def _build_amenities(self):
    bed_count = self.listing_attrs_input.get(BEDROOM_COUNT)
    if not bed_count:
      self.listing_attrs_output[BEDROOM_COUNT] = 1

  def build_listing(self):
    self._build_title()
    self._build_description()
    self._build_general_details()
    self._build_fees()
    self._build_location()
    self._build_contact_details()
    self._build_amenities()

    return factories.construct_listing(**self.listing_attrs_output)

  def _assign_output_attr(self, key, value):
    self.listing_attrs_output[key] = value
