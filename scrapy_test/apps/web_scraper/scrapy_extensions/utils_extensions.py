from dynamic_scraper.utils.task_utils import TaskUtils
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher


# settings are defined in the manage.py file
settings = get_project_settings()
# how to get settings: http://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy


def stop_reactor():
  reactor.stop()


dispatcher.connect(stop_reactor, signal=signals.spider_closed)


class ProcessBasedUtils(TaskUtils):
  def _run_spider(self, **kwargs):
    spider_name = kwargs['spider']
    param_dict = {
      'project': 'default',
      'spider': spider_name,
      'id': kwargs['id'],
      'run_type': kwargs['run_type'],
      'do_action': kwargs['do_action']
    }

    print param_dict

    # region How to run a crawler in-process
    # examples on how to get this stuff:
    # http://stackoverflow.com/questions/14777910/scrapy-crawl-from-script-always-blocks-script-execution-after-scraping?lq=1
    # http://stackoverflow.com/questions/13437402/how-to-run-scrapy-from-within-a-python-script
    # http://stackoverflow.com/questions/7993680/running-scrapy-tasks-in-python
    # http://stackoverflow.com/questions/15564844/locally-run-all-of-the-spiders-in-scrapy
    # https://groups.google.com/forum/#!topic/scrapy-users/d4axj6nPVDw
    # endregion

    crawler = Crawler(settings)
    crawler.configure()
    spider = crawler.spiders.create(spider_name, **kwargs)
    crawler.crawl(spider)
    crawler.start()

    log.start()
    log.msg('Running reactor...')

    reactor.run()  # the script will block here until the spider is closed

    log.msg('Reactor stopped.')

