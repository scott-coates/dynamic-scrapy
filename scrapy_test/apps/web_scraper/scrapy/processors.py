from urlparse import urljoin


#this is called from the admin. The listing spider defins this method as a processor and is invoked dynamically
def pre_url_from_ref_object(text, loader_context):
  base_url = loader_context['spider'].ref_object.listing_source.url

  ret_val = urljoin(base_url, text[0])

  return ret_val
