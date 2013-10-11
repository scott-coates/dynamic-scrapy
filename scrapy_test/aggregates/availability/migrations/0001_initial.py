# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Availability'
        db.create_table(u'availability_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('system_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('aliases', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'availability', ['Availability'])


    def backwards(self, orm):
        # Deleting model 'Availability'
        db.delete_table(u'availability_availability')


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