from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapy.item import BaseItem


class IndividualItemSpider(DjangoSpider):
  def parse(self, response):
    url_elem = self.scraper.get_detail_page_url_elem()

    #multi-detail-hack
    #usually the meta[item] will be empty, but if we are getting the item from a multi-detail request,
    # it's possible this will already be populated by the ListingSpider.parse method,
    # if it's handling the current request off to combine the many detail pages.
    if 'item' not in response.meta:
      #the loader in the DJspider class expects a dict to populate
      response.meta['item'] = self.scraped_obj_item_class()

    item = self.parse_item(response)

    #multi-detail-hack
    #if we are targeting a source that has multiple detail pages, the listing_spider will yield a Request to the next
    #  page in the cycle. All we need to do is tell the Request to call self.parse and not ListingSpider.parse
    if isinstance(item, BaseItem):
      url_name = url_elem.scraped_obj_attr.name
      if item:
        item[url_name] = response.url
        cnt = self.scraped_obj_class.objects.filter(url=item[url_name]).count()
        # Mark item as DOUBLE item
        if cnt > 0:
          item[url_name] = 'DOUBLE' + item[url_name]
        yield item
    else:
      #multi-detail-hack
      # if the ListingSpider.parse is handing this request off so it can combine many detail pages together,
      # we need to call self.parse so we don't call ListingSpider.parse (which has diff logic than this class)
      item.callback = self.parse
      yield item

  def spider_closed(self):
    #hack: we don't want to have our individual scraping change the scheduling of a normal spider
    pass
