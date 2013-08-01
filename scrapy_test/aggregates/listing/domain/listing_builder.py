from scrapy_test.aggregates.listing_source.services import listing_source_service

bedroom_count = 'bedroom_count'
bathroom_count = 'bathroom_count'
sqfeet = 'sqfeet'
price = 'price'
broker_fee = 'broker_fee'


class ListingBuilder(object):
  def __init__(self, **listing_attrs):
    self.listing_attrs_input = listing_attrs
    self.listing_attrs_output = listing_attrs

  def _build_listing_source(self):
    listing_source_id = self.listing_attrs_input.get('listing_source_id')
    if not listing_source_id: raise TypeError('listing_source_id required')
    self.listing_attrs_output['listing_source'] = listing_source_service.get_listing_source(listing_source_id)

  def _build_summary(self):
    """
    description
    title
    """

  def _build_general_details(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

      #bath
      #sqfeet
      #price

  def _build_fees(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

  def _build_location(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

  def _build_contact_details(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

  def _build_amenities(self):
    bed_count = self.listing_attrs_input.get(bedroom_count)
    if not bed_count:
      self.listing_attrs_output[bedroom_count] = 1

  def build_listing(self):
    self._build_listing_source()
    self._build_summary()
    self._build_general_details()
    self._build_fees()
    self._build_location()
    self._build_contact_details()
    self._build_amenities()

    return 'foo'
