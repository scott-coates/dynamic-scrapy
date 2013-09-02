# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Listing.address1'
        db.add_column(u'listing_listing', 'address1',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.address2'
        db.add_column(u'listing_listing', 'address2',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.city'
        db.add_column(u'listing_listing', 'city',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255),
                      keep_default=False)

        # Adding field 'Listing.state'
        db.add_column(u'listing_listing', 'state',
                      self.gf('localflavor.us.models.USStateField')(default=None, max_length=2),
                      keep_default=False)

        # Adding field 'Listing.zip_code'
        db.add_column(u'listing_listing', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.lat'
        db.add_column(u'listing_listing', 'lat',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Listing.lng'
        db.add_column(u'listing_listing', 'lng',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Listing.bedroom_count'
        db.add_column(u'listing_listing', 'bedroom_count',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Listing.bathroom_count'
        db.add_column(u'listing_listing', 'bathroom_count',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Listing.sqfeet'
        db.add_column(u'listing_listing', 'sqfeet',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Listing.price'
        db.add_column(u'listing_listing', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=7, decimal_places=2),
                      keep_default=False)

        # Adding field 'Listing.broker_fee'
        db.add_column(u'listing_listing', 'broker_fee',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Listing.contact_name'
        db.add_column(u'listing_listing', 'contact_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.contact_phone_number'
        db.add_column(u'listing_listing', 'contact_phone_number',
                      self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.contact_email'
        db.add_column(u'listing_listing', 'contact_email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Listing.last_updated_date'
        db.add_column(u'listing_listing', 'last_updated_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(1970, 1, 1, 0, 0)),
                      keep_default=False)

        # Adding field 'Listing.is_dead'
        db.add_column(u'listing_listing', 'is_dead',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Listing.created_date'
        db.add_column(u'listing_listing', 'created_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(1970, 1, 1, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Listing.changed_date'
        db.add_column(u'listing_listing', 'changed_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(1970, 1, 1, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Listing.address1'
        db.delete_column(u'listing_listing', 'address1')

        # Deleting field 'Listing.address2'
        db.delete_column(u'listing_listing', 'address2')

        # Deleting field 'Listing.city'
        db.delete_column(u'listing_listing', 'city')

        # Deleting field 'Listing.state'
        db.delete_column(u'listing_listing', 'state')

        # Deleting field 'Listing.zip_code'
        db.delete_column(u'listing_listing', 'zip_code')

        # Deleting field 'Listing.lat'
        db.delete_column(u'listing_listing', 'lat')

        # Deleting field 'Listing.lng'
        db.delete_column(u'listing_listing', 'lng')

        # Deleting field 'Listing.bedroom_count'
        db.delete_column(u'listing_listing', 'bedroom_count')

        # Deleting field 'Listing.bathroom_count'
        db.delete_column(u'listing_listing', 'bathroom_count')

        # Deleting field 'Listing.sqfeet'
        db.delete_column(u'listing_listing', 'sqfeet')

        # Deleting field 'Listing.price'
        db.delete_column(u'listing_listing', 'price')

        # Deleting field 'Listing.broker_fee'
        db.delete_column(u'listing_listing', 'broker_fee')

        # Deleting field 'Listing.contact_name'
        db.delete_column(u'listing_listing', 'contact_name')

        # Deleting field 'Listing.contact_phone_number'
        db.delete_column(u'listing_listing', 'contact_phone_number')

        # Deleting field 'Listing.contact_email'
        db.delete_column(u'listing_listing', 'contact_email')

        # Deleting field 'Listing.last_updated_date'
        db.delete_column(u'listing_listing', 'last_updated_date')

        # Deleting field 'Listing.is_dead'
        db.delete_column(u'listing_listing', 'is_dead')

        # Deleting field 'Listing.created_date'
        db.delete_column(u'listing_listing', 'created_date')

        # Deleting field 'Listing.changed_date'
        db.delete_column(u'listing_listing', 'changed_date')


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
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_date': ('django.db.models.fields.DateTimeField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'listing_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listing_source.ListingSource']"}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'contact_phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '8000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
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
