# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Amenity'
        db.create_table(u'apartment_amenity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='amenities', to=orm['apartment.Apartment'])),
            ('amenity_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apartment_instance', to=orm['amenity.Amenity'])),
        ))
        db.send_create_signal(u'apartment', ['Amenity'])

        # Adding unique constraint on 'Amenity', fields ['apartment', 'amenity_type']
        db.create_unique(u'apartment_amenity', ['apartment_id', 'amenity_type_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Amenity', fields ['apartment', 'amenity_type']
        db.delete_unique(u'apartment_amenity', ['apartment_id', 'amenity_type_id'])

        # Deleting model 'Amenity'
        db.delete_table(u'apartment_amenity')


    models = {
        u'amenity.amenity': {
            'Meta': {'object_name': 'Amenity'},
            'aliases': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'apartment.amenity': {
            'Meta': {'unique_together': "(('apartment', 'amenity_type'),)", 'object_name': 'Amenity'},
            'amenity_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apartment_instance'", 'to': u"orm['amenity.Amenity']"}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amenities'", 'to': u"orm['apartment.Apartment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'apartment.apartment': {
            'Meta': {'unique_together': "(('lat', 'lng', 'price'),)", 'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bathroom_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'bedroom_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'broker_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'sqfeet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '3', 'blank': 'True'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['apartment']