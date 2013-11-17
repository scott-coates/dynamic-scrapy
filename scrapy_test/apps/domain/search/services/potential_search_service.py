import json
from django.conf import settings
from django.db import transaction
from django.forms import model_to_dict
from scrapy_test.aggregates.search.models import Search
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.signals import potential_search_completed
from scrapy_test.libs.payment_utils.services import payment_service


def save_or_update(potential_search):
  geo_points = potential_search.search_attrs.get('geo_boundary_points')

  if geo_points is not None and len(geo_points) < 1:
    del potential_search.search_attrs['geo_boundary_points']

  potential_search.save(internal=True)


def get_potential_search(pk):
  return PotentialSearch.objects.get(pk=pk)


def get_search_attrs(search_attrs_dict):
  amenities = search_attrs_dict.pop('amenities', None)
  search = Search(**search_attrs_dict)

  search_dict = model_to_dict(search, fields=search_attrs_dict.keys())
  if amenities: search_dict['amenities'] = amenities

  # for some reason, model_to_dict converts the value to a string
  if 'geo_boundary_points' in search_dict:
    search_dict['geo_boundary_points'] = json.loads(search_dict['geo_boundary_points'])

  return search_dict


def complete_potential_search(potential_search, token, _payment_service=payment_service):
  with transaction.commit_on_success():
    customer_email = potential_search.search_attrs['email_address']
    potential_search.purchased = True
    save_or_update(potential_search)
    _payment_service.charge_payment(settings.SEARCH_PRICE, token, "Nextlanding search for {0}.".format(customer_email))

  potential_search_completed.send(PotentialSearch, instance=potential_search)
