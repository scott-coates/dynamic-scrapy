# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Search'
        db.create_table(u'search_search', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('specified_location', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('geo_boundary_points', self.gf('jsonfield.fields.JSONField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('formatted_address', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('no_fee_preferred', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bedroom_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('bedroom_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('bathroom_min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('bathroom_max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('price_min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('price_max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sqfeet_min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('sqfeet_max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'search', ['Search'])

        # Adding model 'Amenity'
        db.create_table(u'search_amenity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search', self.gf('django.db.models.fields.related.ForeignKey')(related_name='amenities', to=orm['search.Search'])),
            ('amenity_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='search_instance', to=orm['amenity.Amenity'])),
        ))
        db.send_create_signal(u'search', ['Amenity'])

        # Adding unique constraint on 'Amenity', fields ['search', 'amenity_type']
        db.create_unique(u'search_amenity', ['search_id', 'amenity_type_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Amenity', fields ['search', 'amenity_type']
        db.delete_unique(u'search_amenity', ['search_id', 'amenity_type_id'])

        # Deleting model 'Search'
        db.delete_table(u'search_search')

        # Deleting model 'Amenity'
        db.delete_table(u'search_amenity')


    models = {
        u'amenity.amenity': {
            'Meta': {'object_name': 'Amenity'},
            'aliases': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'search.amenity': {
            'Meta': {'unique_together': "(('search', 'amenity_type'),)", 'object_name': 'Amenity'},
            'amenity_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'search_instance'", 'to': u"orm['amenity.Amenity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amenities'", 'to': u"orm['search.Search']"})
        },
        u'search.search': {
            'Meta': {'object_name': 'Search'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bathroom_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'bedroom_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'geo_boundary_points': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'no_fee_preferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'specified_location': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'sqfeet_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'sqfeet_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']
