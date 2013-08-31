from scrapy import log
from scrapy.exceptions import DropItem


class ValidationPipeline(object):
  def process_item(self, item, spider):

    url_elem = spider.scraper.get_detail_page_url_elem()
    url_name = url_elem.scraped_obj_attr.name

    mandatory_elems = spider.scraper.get_mandatory_scrape_elems()

    for elem in mandatory_elems:
      if not elem.scraped_obj_attr.name in item or \
          (elem.scraped_obj_attr.name in item and not item[elem.scraped_obj_attr.name]):
        spider.log("Mandatory elem " + elem.scraped_obj_attr.name + " missing!", log.ERROR)
        spider.crawler.stats.inc_value(
          'item_dropped/{0}/{1}/missing_{1}'.format(spider.name, elem.scraped_obj_attr.name)
        )
        raise DropItem()

    if spider.conf['MAX_ITEMS_SAVE'] and spider.items_save_count >= spider.conf['MAX_ITEMS_SAVE']:
      spider.log("Max items save reached, item not saved.", log.INFO)
      raise DropItem()

    if not spider.conf['DO_ACTION']:
      spider.log("TESTMODE: Item not saved.", log.INFO)
      raise DropItem()

    spider.items_save_count += 1

    return item
