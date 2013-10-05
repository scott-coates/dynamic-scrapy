# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Listing.requires_sanity_checking'
        db.add_column(u'listing_listing', 'requires_sanity_checking',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Listing.validation_parsing_errors'
        db.add_column(u'listing_listing', 'validation_parsing_errors',
                      self.gf('jsonfield.fields.JSONField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Listing.requires_sanity_checking'
        db.delete_column(u'listing_listing', 'requires_sanity_checking')

        # Deleting field 'Listing.validation_parsing_errors'
        db.delete_column(u'listing_listing', 'validation_parsing_errors')


    models = {
        u'listing.listing': {
            'Meta': {'object_name': 'Listing'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing_source.ListingSource']"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
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
        }
    }

    complete_apps = ['listing']
