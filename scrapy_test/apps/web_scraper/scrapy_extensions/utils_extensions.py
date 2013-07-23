from dynamic_scraper.utils.task_utils import TaskUtils


class ProcessBasedUtils(TaskUtils):
  def _run_spider(self, **kwargs):
    param_dict = {
      'project': 'default',
      'spider': kwargs['spider'],
      'id': kwargs['id'],
      'run_type': kwargs['run_type'],
      'do_action': kwargs['do_action']
    }

    print param_dict
