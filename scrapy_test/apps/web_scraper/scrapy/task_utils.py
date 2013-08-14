from dynamic_scraper.utils.task_utils import ProcessBasedUtils


class IndividualItemLauncher(object):
  def run_spider(self, spider_name, url):
    raise NotImplementedError('This function must be overriden')


class IndividualProcessBasedItemLauncher(IndividualItemLauncher, ProcessBasedUtils):
  def run_spider(self, spider_name, url):
    super(IndividualProcessBasedItemLauncher, self)._run_spider(run_type='TASK', do_action='yes')
    self._run_spider(spider=spider_name, url=url)

