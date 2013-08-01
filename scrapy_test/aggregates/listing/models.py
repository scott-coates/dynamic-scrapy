from django.db import models
import logging
from localflavor.us.models import USStateField, PhoneNumberField
from scrapy_test.aggregates.listing_source.models import ListingSource

logger = logging.getLogger(__name__)


class Listing(models.Model):
  """
  todo:
  - local flav fields
  - I removed a bunch of nullable stuff (review)
  - amenities
  """

  listing_source = models.ForeignKey(ListingSource)

  title = models.CharField(max_length=8000)
  description = models.TextField()

  url = models.URLField()

  address1 = models.CharField(max_length=255, blank=True, null=True)
  address2 = models.CharField(max_length=255, blank=True, null=True)
  # city__strip = cltags.get('city', '').strip()
  # #sometimes people put in tons of cities like "Astoria,Brooklyn,....
  # if city__strip and len(city__strip) <= max_city_length: listing.city = city__strip
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()

  bedroom = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  bathroom = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  broker_fee = models.BooleanField()

  contact_name = models.CharField(max_length=255, blank=True, null=True)
  phone_number = PhoneNumberField(blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

  last_updated = models.DateTimeField()

  # requires_sanity_checking = models.BooleanField()
  # validation_parsing_errors = jsonfield.JSONField(blank=True, null=True)

  # apartment    = models.ForeignKey('apartment.Apartment', related_name='listings', blank=True, null=True)
  #
  # crawl    = models.ForeignKey('crawl.Crawl', related_name='listings', blank=True, null=True)
  #
  # amenities = dbarray.TextArrayField(blank=True, null=True)
  # pets               = models.ManyToManyField('pet.Pet',                          blank=True, null=True)
  # building_amenities = models.ManyToManyField('building_amenity.BuildingAmenity', blank=True, null=True)
  # building_types     = models.ManyToManyField('building_type.BuildingType',       blank=True, null=True)
  # unit_amenities     = models.ManyToManyField('unit_amenity.UnitAmenity',         blank=True, null=True)
  # unit_types         = models.ManyToManyField('unit_type.UnitType',               blank=True, null=True)

  is_alive = models.BooleanField()

  created = models.DateTimeField(auto_now_add=True)
  changed = models.DateTimeField(auto_now=True)


  def __unicode__(self):
    return self.title

  def save(self, internal=False, *args, **kwargs):
    if internal:
      super(Listing, self).save(*args, **kwargs)
    else:
      from scrapy_test.aggregates.listing.services import listing_service
      listing_service.save_or_update(self)
