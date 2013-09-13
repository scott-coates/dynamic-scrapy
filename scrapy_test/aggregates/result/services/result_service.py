from scrapy_test.aggregates.result import factories


def create_result(apartment, listing):
  result = factories.construct_result(apartment, listing)

  save_or_update(result)

  return result


def save_or_update(result):
  result.save(internal=True)
