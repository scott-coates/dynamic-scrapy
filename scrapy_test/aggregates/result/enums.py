from scrapy_test.libs.python_utils.types.enum import enum

AvailabilityStatusEnum = enum(
  Available=1,
  Unavailable=2,
  #another tenant found this apartment to be unavailable
  DifferentUserNotifiedUnavailable=3,
)

AvailabilityStatusChoices = (
  (AvailabilityStatusEnum.Available, 'Is Available'),
  (AvailabilityStatusEnum.Unavailable, 'Is Unavailable'),
  (AvailabilityStatusEnum.DifferentUserNotifiedUnavailable, 'Another user was notified unavailable'),
)
