from django.db import models, transaction
from reversion.models import Revision


class Event(models.Model):
  revision = models.OneToOneField(Revision)
  version = models.PositiveIntegerField()
  name = models.CharField(max_length=1024)
