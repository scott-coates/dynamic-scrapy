import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapy_test.settings.dev") #Changed in DDS v.0.3

BOT_NAME = 'scrapy_test'

SPIDER_MODULES = [
  'dynamic_scraper.spiders',
  'scrapy_test.apps.web_scraper.spiders',
  'scrapy_test.apps.web_scraper.checkers',
]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
  'scrapy_test.apps.web_scraper.pipelines.validation_pipeline.ValidationPipeline',
  'scrapy_test.apps.web_scraper.pipelines.aggregate_writer_pipeline.AggregateCommandPipeline',
]

EXTENSIONS = {
  'scrapy_test.apps.web_scraper.scrapy.extensions.StopOnDuplicateItem': 500,
  'scrapy_test.apps.web_scraper.scrapy.extensions.StatsReporter': 500,
}

DOWNLOADER_MIDDLEWARES = {
  'scrapy_test.apps.web_scraper.scrapy.middlewares.ProxyMiddleware': 755,
  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
}

# https://scrapy.readthedocs.org/en/latest/topics/settings.html#randomize-download-delay
DOWNLOAD_DELAY = 0.73
