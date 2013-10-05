# this was the only way to avoid a circular import because
# communication_associater -> search -> communication_associater

from scrapy_test.apps.communication_associater import event_handlers
