from django.db import models
from reversion.models import Revision


class Event(models.Model):
  revision  = models.ForeignKey(Revision)
  version = models.PositiveIntegerField()
  name = models.CharField(max_length=1024)
