from multiprocessing import Process
from dynamic_scraper.utils.task_utils import TaskUtils
from scrapy import log
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# settings are defined in the manage.py file
settings = get_project_settings()
# how to get settings: http://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy


class ProcessBasedUtils(TaskUtils):
  def testabc(self, **kwargs):
    # region How to run a crawler in-process
    # examples on how to get this stuff:
    # http://stackoverflow.com/questions/14777910/scrapy-crawl-from-script-always-blocks-script-execution-after-scraping?lq=1
    # http://stackoverflow.com/questions/13437402/how-to-run-scrapy-from-within-a-python-script
    # http://stackoverflow.com/questions/7993680/running-scrapy-tasks-in-python
    # http://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy
    # https://groups.google.com/forum/#!topic/scrapy-users/d4axj6nPVDw
    # endregion

    crawler = CrawlerProcess(settings)
    crawler.install()
    crawler.configure()
    spider = crawler.spiders.create(kwargs['spider'], **kwargs)
    crawler.crawl(spider)

    log.start()
    log.msg('Spider started...')
    crawler.start()
    log.msg('Spider stopped.')
    crawler.stop()

  def _run_spider(self, **kwargs):
    param_dict = {
      'project': 'default',
      'spider': kwargs['spider'],
      'id': kwargs['id'],
      'run_type': kwargs['run_type'],
      'do_action': kwargs['do_action']
    }

    p = Process(target=self.testabc, kwargs=param_dict)
    p.start()
    p.join()

