# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from scrapy_test.libs.django_utils.extensions.migrations import load_data


class Migration(DataMigration):

    def forwards(self, orm):
      load_data(orm, "0002_availability_import.json")


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
      u'availability.availability': {
        'Meta': {'object_name': 'Availability'},
        'aliases': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
        u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
        'system_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
      }
    }


    complete_apps = ['availability']
    symmetrical = True
