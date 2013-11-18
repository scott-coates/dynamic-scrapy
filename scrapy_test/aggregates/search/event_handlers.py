from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import became_unavailable
from scrapy_test.aggregates.result.services import result_tasks
from scrapy_test.aggregates.search.services import search_tasks
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.signals import potential_search_completed
from scrapy_test.libs.communication_utils.models import Email
from scrapy_test.libs.communication_utils.signals import email_received


@receiver(potential_search_completed, sender=PotentialSearch)
def potential_search_completed_callback(sender, **kwargs):
  search_tasks.create_search_task.delay(**kwargs['instance'].search_attrs)
