import logging

from django.db import models, transaction
from localflavor.us.models import USStateField
import reversion
from scrapy_test.aggregates.apartment.enums import ApartmentUnavailableReasonEnum

from scrapy_test.aggregates.apartment.managers import ApartmentManager
from scrapy_test.aggregates.apartment.signals import adopted_listing, became_unavailable, created_from_listing
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.common_domain.models import RevisionEvent
from scrapy_test.libs.django_utils.serialization.flexible_json_serializer import JSONSerializer


logger = logging.getLogger(__name__)


class Apartment(models.Model, AggregateBase):
  objects = ApartmentManager()

  address = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  formatted_address = models.CharField(max_length=4096)

  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  broker_fee = models.BooleanField()

  #can this apartment be rented?
  is_available = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ("lat", "lng", "price")

  def __init__(self, *args, **kwargs):
    super(Apartment, self).__init__(*args, **kwargs)
    self._amenity_list = []

  @classmethod
  def _from_listing(cls, listing):
    ret_val = cls()

    if not listing:
      raise TypeError("listing is required")

    ret_val._raise_event(created_from_listing, sender=Apartment, instance=ret_val, listing=listing)

    return ret_val

  def adopt_listing(self, listing):
    self._raise_event(adopted_listing, sender=Apartment, instance=self, listing=listing)

  def _handle_created_from_listing_event(self, listing, **kwargs):
    self._handle_adopted_listing_event(listing, **kwargs)

  def _handle_adopted_listing_event(self, listing, **kwargs):
    self.address = self.address or listing.address
    self.city = self.city or listing.city
    self.state = self.state or listing.state
    self.zip_code = self.zip_code or listing.zip_code
    self.lat = self.lat or listing.lat
    self.lng = self.lng or listing.lng
    self.formatted_address = self.formatted_address or listing.formatted_address

    self.bedroom_count = self.bedroom_count or listing.bedroom_count
    self.bathroom_count = self.bathroom_count or listing.bathroom_count
    self.sqfeet = self.sqfeet or listing.sqfeet
    self.price = self.price or listing.price
    self.broker_fee = self.broker_fee or listing.broker_fee

    existing_amenities = self.amenities.values_list('amenity_type_id', flat=True)
    self._amenity_list.extend(
      Amenity(amenity_type_id=a.amenity_type_id, is_available=a.is_available) for a in listing.amenities.all() if
      a.amenity_type_id not in existing_amenities
    )

    self.is_available = True

  def update_availability(self):
    if all(l.is_dead or l.is_deleted for l in self.listings.all()):
      self._make_unavailable(ApartmentUnavailableReasonEnum.AllListingsUnavailable)

  def notify_unavailable(self):
    self._make_unavailable(ApartmentUnavailableReasonEnum.NotifiedUnavailable)

  def _make_unavailable(self, reason):
    self._raise_event(became_unavailable, sender=Apartment, instance=self, reason=reason)

  def _handle_became_unavailable_event(self, **kwargs):
    self.is_available = False

  def __unicode__(self):
    return 'Apartment #' + str(self.pk) + ': ' + self.formatted_address

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        with reversion.create_revision():
          super(Apartment, self).save(*args, **kwargs)

          for a in self._amenity_list:
            #add actually does a save internally, hitting the db
            self.amenities.add(a)

          serializer = JSONSerializer()

          for event in self._uncommitted_events:
            #we don't need to store the instance because it's not really part of the parameters
            #and django-reversion will keep a snapshop
            kwargs_to_save= {k: v for k, v in event.kwargs.items() if k != 'instance'}
            data = serializer.serialize(kwargs_to_save)

            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version, data=data)

      self.send_events()
    else:
      from scrapy_test.aggregates.apartment.services import apartment_service

      apartment_service.save_or_update(self)


class Amenity(models.Model):
  is_available = models.BooleanField()
  apartment = models.ForeignKey(Apartment, related_name='amenities')
  amenity_type = models.ForeignKey('amenity.Amenity', related_name='apartment_instance')

  class Meta:
    unique_together = ("apartment", "amenity_type")
