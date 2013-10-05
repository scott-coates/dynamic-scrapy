# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ListingSourceScraperConfig.id'
        db.delete_column(u'web_scraper_listingsourcescraperconfig', u'id')


        # Changing field 'ListingSourceScraperConfig.scraper_runtime'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'scraper_runtime_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dynamic_scraper.SchedulerRuntime'], unique=True, null=True, on_delete=models.SET_NULL))
        # Adding unique constraint on 'ListingSourceScraperConfig', fields ['scraper_runtime']
        db.create_unique(u'web_scraper_listingsourcescraperconfig', ['scraper_runtime_id'])


        # Changing field 'ListingSourceScraperConfig.scraper'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'scraper_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dynamic_scraper.Scraper'], unique=True, null=True, on_delete=models.SET_NULL))
        # Adding unique constraint on 'ListingSourceScraperConfig', fields ['scraper']
        db.create_unique(u'web_scraper_listingsourcescraperconfig', ['scraper_id'])


        # Changing field 'ListingSourceScraperConfig.listing_source'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'listing_source_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['listing_source.ListingSource'], unique=True, primary_key=True))
        # Adding unique constraint on 'ListingSourceScraperConfig', fields ['listing_source']
        db.create_unique(u'web_scraper_listingsourcescraperconfig', ['listing_source_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ListingSourceScraperConfig', fields ['listing_source']
        db.delete_unique(u'web_scraper_listingsourcescraperconfig', ['listing_source_id'])

        # Removing unique constraint on 'ListingSourceScraperConfig', fields ['scraper']
        db.delete_unique(u'web_scraper_listingsourcescraperconfig', ['scraper_id'])

        # Removing unique constraint on 'ListingSourceScraperConfig', fields ['scraper_runtime']
        db.delete_unique(u'web_scraper_listingsourcescraperconfig', ['scraper_runtime_id'])

        # Adding field 'ListingSourceScraperConfig.id'
        db.add_column(u'web_scraper_listingsourcescraperconfig', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)


        # Changing field 'ListingSourceScraperConfig.scraper_runtime'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'scraper_runtime_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dynamic_scraper.SchedulerRuntime'], null=True, on_delete=models.SET_NULL))

        # Changing field 'ListingSourceScraperConfig.scraper'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'scraper_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dynamic_scraper.Scraper'], null=True, on_delete=models.SET_NULL))

        # Changing field 'ListingSourceScraperConfig.listing_source'
        db.alter_column(u'web_scraper_listingsourcescraperconfig', 'listing_source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listing_source.ListingSource']))

    models = {
        u'apartment.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
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
            'checker_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 1440,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 1,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 5,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scraper_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 15,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 10,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 20,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''})
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
            'scraped_obj_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dynamic_scraper.ScrapedObjClass']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        u'listing.listing': {
            'Meta': {'object_name': 'Listing'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'listings'", 'null': 'True', 'to': u"orm['apartment.Apartment']"}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing_source.ListingSource']"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'posted_date': ('django.db.models.fields.DateTimeField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'requires_sanity_checking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'validation_parsing_errors': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'listing_source.listingsource': {
            'Meta': {'object_name': 'ListingSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'web_scraper.listingcheckerconfig': {
            'Meta': {'object_name': 'ListingCheckerConfig'},
            'checker_runtime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing.Listing']"})
        },
        u'web_scraper.listingsourcescraperconfig': {
            'Meta': {'object_name': 'ListingSourceScraperConfig'},
            'listing_source': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listing_source.ListingSource']", 'unique': 'True', 'primary_key': 'True'}),
            'scraper': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dynamic_scraper.Scraper']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'scraper_runtime': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dynamic_scraper.SchedulerRuntime']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['web_scraper']
