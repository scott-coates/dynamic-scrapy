# -*- coding: utf-8 -*-
from south.v2 import DataMigration
from scrapy_test.libs.django_utils.extensions.migrations import load_data


class Migration(DataMigration):
  def forwards(self, orm):
    load_data(orm, "0005_add_street_easy.json")


  def backwards(self, orm):
    "Write your backwards methods here."

  models = {
    u'listing_source.listingsource': {
      'Meta': {'object_name': 'ListingSource'},
      u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'trusted_geo_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
    }
  }

  complete_apps = ['listing_source']
  symmetrical = True
