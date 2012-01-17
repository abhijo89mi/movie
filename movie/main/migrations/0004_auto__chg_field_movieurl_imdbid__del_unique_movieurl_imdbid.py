# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'movieurl.imdbid'
        db.alter_column('main_movieurl', 'imdbid', self.gf('django.db.models.fields.SlugField')(max_length=200))

        # Adding index on 'movieurl', fields ['imdbid']
        db.create_index('main_movieurl', ['imdbid'])

        # Removing unique constraint on 'movieurl', fields ['imdbid']
        db.delete_unique('main_movieurl', ['imdbid'])


    def backwards(self, orm):
        
        # Changing field 'movieurl.imdbid'
        db.alter_column('main_movieurl', 'imdbid', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True))

        # Removing index on 'movieurl', fields ['imdbid']
        db.delete_index('main_movieurl', ['imdbid'])

        # Adding unique constraint on 'movieurl', fields ['imdbid']
        db.create_unique('main_movieurl', ['imdbid'])


    models = {
        'main.errorlog': {
            'Meta': {'object_name': 'Errorlog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'function_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'main.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'total_movie': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.movieurl': {
            'Meta': {'object_name': 'movieurl'},
            'filter_based_on': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Genre']", 'to_field': "'name'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdbid': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'last_rundate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'movie_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'run_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'runcount': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'sucess_factor': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'main.urllog': {
            'Meta': {'object_name': 'Urllog'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_url_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_url_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']
