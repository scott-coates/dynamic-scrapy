# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Listing.title'
        db.alter_column(u'listing_listing', 'title', self.gf('django.db.models.fields.CharField')(max_length=8000))

    def backwards(self, orm):

        # Changing field 'Listing.title'
        db.alter_column(u'listing_listing', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'listing.listing': {
            'Meta': {'object_name': 'Listing'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing_source.ListingSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listing']