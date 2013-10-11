# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PotentialSearch'
        db.create_table(u'domain_potentialsearch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_attrs', self.gf('jsonfield.fields.JSONField')()),
            ('purchased', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('domain', ['PotentialSearch'])


    def backwards(self, orm):
        # Deleting model 'PotentialSearch'
        db.delete_table(u'domain_potentialsearch')


    models = {
        'domain.potentialsearch': {
            'Meta': {'object_name': 'PotentialSearch'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_attrs': ('jsonfield.fields.JSONField', [], {})
        }
    }

    complete_apps = ['domain']
