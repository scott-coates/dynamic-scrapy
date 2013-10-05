from scrapy_test.libs.python_utils.types.enum import enum

DeletedListingReasonEnum = enum(
  #did we manually delete it?
  AdminDeleted=1,
  #was the listing no longer alive? Was it returning 404 or did it convey the apartment was no longer available?
  DeadListing=2,
  #notified unavailable by external party
  NotifiedUnavailable=3,
)

DeletedListingReasonChoices = (
  (DeletedListingReasonEnum.AdminDeleted, 'Admin Deleted'),
  (DeletedListingReasonEnum.DeadListing, 'Dead Listing'),
  (DeletedListingReasonEnum.NotifiedUnavailable, 'Notified Unavailable'),
)
