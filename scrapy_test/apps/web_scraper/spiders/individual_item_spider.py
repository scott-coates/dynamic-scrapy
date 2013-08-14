from dynamic_scraper.spiders.django_spider import DjangoSpider


class IndividualItemSpider(DjangoSpider):
  def parse(self, response):
    url_elem = self.scraper.get_detail_page_url_elem()
    response.request.meta['item'] = self.scraped_obj_item_class()
    item = self.parse_item(response)
    url_name = url_elem.scraped_obj_attr.name
    if item:
      item[url_name] = response.url
      cnt = self.scraped_obj_class.objects.filter(url=item[url_name]).count()
      # Mark item as DOUBLE item
      if cnt > 0:
        item[url_name] = 'DOUBLE' + item[url_name]
      yield item
