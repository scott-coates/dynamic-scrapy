from dynamic_scraper.utils import processors

#todo put this in a fork and pull request
def pre_url_from_ref_object(text, loader_context):
  from urlparse import urljoin

  base_url = loader_context['spider'].ref_object.url

  ret_val = urljoin(base_url, text)

  return ret_val


setattr(processors, 'pre_url_from_ref_object', pre_url_from_ref_object)
