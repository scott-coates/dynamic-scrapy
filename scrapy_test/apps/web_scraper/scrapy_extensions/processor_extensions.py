from urlparse import urljoin


def pre_url_from_ref_object(text, loader_context):
  base_url = loader_context['spider'].ref_object.listing_source.url

  ret_val = urljoin(base_url, text)

  return ret_val
