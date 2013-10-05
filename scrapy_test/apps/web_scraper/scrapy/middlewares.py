import base64
from django.conf import settings

from scrapy.exceptions import NotConfigured


class ProxyMiddleware(object):
  def __init__(self):

    proxy_username = getattr(settings, 'PROXY_USERNAME', '')
    proxy_password = getattr(settings, 'PROXY_PASSWORD', '')
    proxy_host = getattr(settings, 'PROXY_HOST', '')

    if proxy_username and proxy_password and proxy_host:
      self.proxy_auth_header = (
        'Basic ' + base64.encodestring('%s:%s' % (proxy_username, proxy_password)).replace('\n', '')
      )
      self.proxy_host = proxy_host
    else:
      raise NotConfigured

  def process_request(self, request, spider):
    # ignore if proxy is already seted
    if 'proxy' not in request.meta:
      if 'craigslist' in request.url:
        self._set_proxy(request)


  def _set_proxy(self, request):
    request.meta['proxy'] = self.proxy_host
    request.headers['Authorization'] = self.proxy_auth_header
