# -*- coding: utf-8 -*-
from south.v2 import DataMigration
from scrapy_test.libs.database.extensions.migrations import load_data


class Migration(DataMigration):
  depends_on = (("web_scraper", "0001_initial"),)

  def forwards(self, orm):
    load_data(orm,"0002_load_ny_craigslist_listing_source.json")

  def backwards(self, orm):
    "Write your backwards methods here."

  models = {
    u'dynamic_scraper.schedulerruntime': {
      'Meta': {'ordering': "['next_action_time']", 'object_name': 'SchedulerRuntime'},
      u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'next_action_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
      'next_action_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
      'num_zero_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
      'runtime_type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
    },
    u'dynamic_scraper.scrapedobjclass': {
      'Meta': {'ordering': "['name']", 'object_name': 'ScrapedObjClass'},
      'checker_scheduler_conf': ('django.db.models.fields.TextField', [], {
      'default': '\'"MIN_TIME": 1440,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 1,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 5,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''}),
      'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
      u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'scraper_scheduler_conf': ('django.db.models.fields.TextField', [], {
      'default': '\'"MIN_TIME": 15,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 10,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 20,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''})
    },
    u'dynamic_scraper.scraper': {
      'Meta': {'ordering': "['name', 'scraped_obj_class']", 'object_name': 'Scraper'},
      'checker_ref_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
      'checker_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
      'checker_x_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
      'checker_x_path_result': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
      'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
      'content_type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
      u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'max_items_read': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
      'max_items_save': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'pagination_append_str': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
      'pagination_on_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'pagination_page_replace': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
      'pagination_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
      'scraped_obj_class': (
      'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dynamic_scraper.ScrapedObjClass']"}),
      'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
    },
    u'listing_source.listingsource': {
      'Meta': {'object_name': 'ListingSource'},
      u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'scraper': ('django.db.models.fields.related.ForeignKey', [],
                  {'to': u"orm['dynamic_scraper.Scraper']", 'null': 'True', 'on_delete': 'models.SET_NULL',
                   'blank': 'True'}),
      'scraper_runtime': ('django.db.models.fields.related.ForeignKey', [],
                          {'to': u"orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True',
                           'on_delete': 'models.SET_NULL', 'blank': 'True'}),
      'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
    }
  }

  complete_apps = ['listing_source']
  symmetrical = True
