from dynamic_scraper.utils.task_utils import ProcessBasedUtils


class IndividualItemLauncher(object):
  def run_spider(self, spider_name, url):
    raise NotImplementedError('This function must be overriden')


class IndividualProcessBasedItemLauncher(IndividualItemLauncher, ProcessBasedUtils):
  def run_spider(self, spider_name, url):
    #hack process based utils expects id to be a primary key, but we're passing in a url
    #if we just passed in url, processbased utils would not forward it onto the crawler process
    super(IndividualProcessBasedItemLauncher, self)._run_spider(
      id=url, run_type='TASK', do_action='yes', spider=spider_name
    )
