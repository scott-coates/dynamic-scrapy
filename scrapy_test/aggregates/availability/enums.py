from scrapy_test.libs.python_utils.types.enum import enum

AvailabilityStatusEnum = enum(
  Available='available',
  Unavailable='unavailable',
  #another tenant found this apartment to be unavailable
  DifferentUserNotifiedUnavailable='different_user_notified_unavailable',
)
