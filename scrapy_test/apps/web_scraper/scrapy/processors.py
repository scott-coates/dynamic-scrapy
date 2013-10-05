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
  ret_val = []

  for x in text:
    ret_val.append(x[::-1])

  return ret_val


def split_reverse(text, loader_context):
  ret_val = []

  split_reverse_str = loader_context.get('split_reverse', '')

  for x in text:
    split_list = reversed(x.split(split_reverse_str))
    ret_val.append(split_reverse_str.join(split_list))

  return ret_val


def pre_string(text, loader_context):
  ret_val = []
  pre_str = loader_context.get('pre_string', '')

  for x in text:
    ret_val.append(pre_str + x)

  return ret_val


def post_string(text, loader_context):
  post_str = loader_context.get('post_string', '')
  ret_val = []

  for x in text:
    ret_val.append(x + post_str)

  return ret_val


def composite_func(text, loader_context):
  funcs = loader_context.pop('funcs')

  for f in funcs:
    loader_context['func'] = f
    text = processors.dynamic(text, loader_context)

  return text
