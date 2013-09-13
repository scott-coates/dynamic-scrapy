from scrapy_test.aggregates.result import factories


def create_result(apartment, listing):
  pass


def save_or_update(result):
  result.save(internal=True)
