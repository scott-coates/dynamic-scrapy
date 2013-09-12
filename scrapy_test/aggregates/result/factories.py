from scrapy_test.aggregates.result.models import Result


def construct_result(**kwargs):
  result = result._from_attrs(**kwargs)
  return result
