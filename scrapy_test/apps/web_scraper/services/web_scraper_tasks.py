from celery.task import task
from scrapy_test.apps.web_scraper.services import web_scraper_service


@task()
def run_spiders_task():
  web_scraper_service.run_spiders()
