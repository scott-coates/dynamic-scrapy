from celery.task import task
from scrapy_test.apps.web_scraper.services import web_scraper_service


@task()
def run_spiders_task():
  web_scraper_service.run_spiders()

@task()
def add_listing_checker_task(listing_id):
  return web_scraper_service.add_listing_checker(listing_id).id
