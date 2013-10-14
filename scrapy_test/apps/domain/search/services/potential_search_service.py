import json
from django.forms import model_to_dict
from scrapy_test.aggregates.search.models import Search
from scrapy_test.apps.domain.search.models import PotentialSearch


def save_or_update(potential_search):
  potential_search.save(internal=True)


def get_potential_search(pk):
  return PotentialSearch.objects.get(pk=pk)


def get_search_attrs(search_attrs_dict):
  search = Search(**search_attrs_dict)

  search_dict = model_to_dict(search, fields=search_attrs_dict.keys())

  # for some reason, model_to_dict converts the value to a string
  if 'geo_boundary_points' in search_dict:
    search_dict['geo_boundary_points']  = json.loads(search_dict['geo_boundary_points'])

  return search_dict
