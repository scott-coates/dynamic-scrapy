import logging

from django.db import models


logger = logging.getLogger(__name__)


class ListingSource(models.Model):
  name = models.CharField(max_length=200, unique=True)
  url = models.URLField()
  trusted_geo_data = models.BooleanField()

  def __unicode__(self):
    return self.name
