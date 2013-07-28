import os, sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapy_test.settings.dev") #Changed in DDS v.0.3

BOT_NAME = 'scrapy_test'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'apps.web_scraper.spiders',]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'scrapy_test.apps.web_scraper.pipelines.aggregate_writer_pipeline.AggregateCommandPipeline',
]

EXTENSIONS = {
  'scrapy_test.apps.web_scraper.scrapy.extensions.StopOnDuplicateItem': 500,
}
