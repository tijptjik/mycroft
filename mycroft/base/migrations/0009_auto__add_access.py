# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Access'
        db.create_table('base_access', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('lecture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Lecture'])),
            ('activation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('base', ['Access'])


    def backwards(self, orm):
        # Deleting model 'Access'
        db.delete_table('base_access')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'base.access': {
            'Meta': {'object_name': 'Access'},
            'activation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Lecture']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'base.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Lecturer']"}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Poem']"}),
            'preview': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Preview']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Product']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Series']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '40'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'transcript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Video']"})
        },
        'base.lecturer': {
            'Meta': {'object_name': 'Lecturer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'base.poem': {
            'Meta': {'object_name': 'Poem'},
            'copyright': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Poet']"}),
            'pub_year': ('django.db.models.fields.IntegerField', [], {'default': '1900'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'base.poet': {
            'Meta': {'object_name': 'Poet'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'This is the story of this particular poet'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'default': "'English'", 'max_length': '50'}),
            'year_of_birth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year_of_death': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'base.preview': {
            'Meta': {'object_name': 'Preview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vimeo_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'base.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_in_dollars': ('django.db.models.fields.DecimalField', [], {'default': '4.99', 'max_digits': '5', 'decimal_places': '2'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sold': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'base.series': {
            'Meta': {'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Mycroft Online Lectures'", 'max_length': '100'})
        },
        'base.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'credentials': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'profession': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '1'}),
            'published_work': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'published_work_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'base.video': {
            'Meta': {'object_name': 'Video'},
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '3600'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'subtitle_language': ('django.db.models.fields.CharField', [], {'default': "'English'", 'max_length': '20'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']