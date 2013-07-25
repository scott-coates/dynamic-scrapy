# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ListingSource.scraper_runtime'
        db.delete_column(u'listing_source_listingsource', 'scraper_runtime_id')

        # Deleting field 'ListingSource.scraper'
        db.delete_column(u'listing_source_listingsource', 'scraper_id')


    def backwards(self, orm):
        # Adding field 'ListingSource.scraper_runtime'
        db.add_column(u'listing_source_listingsource', 'scraper_runtime',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dynamic_scraper.SchedulerRuntime'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)

        # Adding field 'ListingSource.scraper'
        db.add_column(u'listing_source_listingsource', 'scraper',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dynamic_scraper.Scraper'], null=True, on_delete=models.SET_NULL, blank=True),
                      keep_default=False)


    models = {
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listing_source']
