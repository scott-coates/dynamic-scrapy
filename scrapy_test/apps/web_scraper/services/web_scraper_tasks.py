from celery.task import task
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.apps.web_scraper.services import web_scraper_service


@task()
def run_spiders_task():
  web_scraper_service.run_spiders()


@task()
def run_checkers_task():
  web_scraper_service.run_checkers()


@task()
def add_listing_checker_task(listing_id):
  listing = listing_service.get_listing(listing_id)

  return web_scraper_service.add_listing_checker(listing).pk


@task()
def delete_listing_checker_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  web_scraper_service.delete_listing_checker(listing)

