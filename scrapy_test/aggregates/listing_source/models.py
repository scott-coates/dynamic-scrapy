from django.db import models
import logging

logger = logging.getLogger(__name__)


class ListingSource(models.Model):
  name = models.CharField(max_length=200)
  url = models.URLField()
  trusted_geo_data = models.BooleanField()

  def __unicode__(self):
    return self.name
