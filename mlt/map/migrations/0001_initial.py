# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Parcel'
        db.create_table('map_parcel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pl', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=27)),
            ('first_owner', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('classcode', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=3438)),
        ))
        db.send_create_signal('map', ['Parcel'])


    def backwards(self, orm):
        
        # Deleting model 'Parcel'
        db.delete_table('map_parcel')


    models = {
        'map.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '27'}),
            'classcode': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'first_owner': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3438'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pl': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['map']
