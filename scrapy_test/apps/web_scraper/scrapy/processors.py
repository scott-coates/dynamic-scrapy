from urlparse import urljoin
from dynamic_scraper.utils import processors

#this is called from the admin. The listing spider defines this method as a processor and is invoked dynamically
def pre_url_from_ref_object(text, loader_context):
  base_url = loader_context['spider'].ref_object.listing_source.url

  ret_val = urljoin(base_url, text[0])

  return ret_val


def replace(text, loader_context):
  ret_val = []

  for x in text:
    for k, v in loader_context['replace'].items():
      x = x.replace(k, v)
    ret_val.append(x)

  return ret_val


def reverse(text, loader_context):
  return text[::-1]


def composite_func(text, loader_context):
  funcs = loader_context.pop('funcs')

  for f in funcs:
    loader_context['func'] = f
    text = processors.dynamic(text, loader_context)

  return text
