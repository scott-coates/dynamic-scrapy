import logging

from django.db import models, transaction
from localflavor.us.models import USStateField
import reversion

from scrapy_test.aggregates.apartment.managers import ApartmentManager
from scrapy_test.aggregates.apartment.signals import adopted_listing
from scrapy_test.libs.common_domain.aggregate_base import AggregateBase
from scrapy_test.libs.common_domain.models import RevisionEvent


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
  sqfeet = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  broker_fee = models.BooleanField()

  #can this apartment be rented?
  is_available = models.BooleanField()

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ("lat", "lng", "price")

  def adopt_listing(self, listing):
    self._raise_event(adopted_listing, sender=Apartment, instance=self, listing=listing)

  def _handle_adopted_listing_event(self, listing, **kwargs):
    self._listing_list.append(listing)

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

    self.is_available = True

  def __unicode__(self):
    return 'Apartment #' + str(self.pk) + ': ' + self.formatted_address

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        with reversion.create_revision():
          super(Apartment, self).save(*args, **kwargs)

          for event in self._uncommitted_events:
            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version)

      self.send_events()
    else:
      from scrapy_test.aggregates.apartment.services import apartment_service

      apartment_service.save_or_update(self)
