from scrapy_test.aggregates.search import factories


def create_search(**search_attrs):
  search = factories.construct_apartment_from_listing(**search_attrs)

  return search

def save_or_update(search):
  search.save(internal=True)
