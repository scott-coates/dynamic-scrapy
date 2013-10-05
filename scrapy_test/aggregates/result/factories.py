from scrapy_test.aggregates.result.models import Result


def construct_result(apartment, search):
  result = Result._from_apartment_and_search(apartment,search)
  return result
