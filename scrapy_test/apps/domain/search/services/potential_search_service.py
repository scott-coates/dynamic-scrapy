from django.forms import model_to_dict
from scrapy_test.aggregates.search.models import Search


def save_or_update(potential_search):
  potential_search.save(internal=True)


def get_search_attrs(search_attrs_dict):
  return model_to_dict(Search(**search_attrs_dict), fields=search_attrs_dict.keys())
