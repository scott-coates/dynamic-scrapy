import os

from dynamic_scraper.spiders.django_checker import DjangoChecker
from scrapy.utils.project import get_project_settings
from dynamic_scraper.models import ScraperElem
from scrapy import log
from scrapy_test.aggregates.listing.services import listing_tasks

from scrapy_test.apps.web_scraper.models import ListingCheckerConfig


settings = get_project_settings()


class ListingChecker(DjangoChecker):
  name = 'listing_checker'

  def __init__(self, *args, **kwargs):
    self._set_ref_object(ListingCheckerConfig, **kwargs)
    self.scraper = self.ref_object.scraper
    self.scrape_url = self.ref_object.listing.url
    self.scheduler_runtime = self.ref_object.checker_runtime
    super(ListingChecker, self).__init__(self, *args, **kwargs)

  def _del_ref_object(self):
    try:
      img_elem = self.scraper.get_image_elem()
      if hasattr(self.ref_object, img_elem.scraped_obj_attr.name):
        img_name = getattr(self.ref_object, img_elem.scraped_obj_attr.name)
        path = os.path.join(settings.get('IMAGES_STORE'), img_name)
        if os.access(path, os.F_OK):
          try:
            os.unlink(path)
            self.log("Associated image deleted.", log.INFO)
          except Exception:
            self.log("Associated image could not be deleted!", log.ERROR)
    except ScraperElem.DoesNotExist:
      pass

    listing_tasks.kill_listing_task.delay(self.ref_object.listing.id)
    self.action_successful = True
    self.log("Item deleted.", log.INFO)
