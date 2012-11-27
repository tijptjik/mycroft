# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('base_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price_in_dollars', self.gf('django.db.models.fields.DecimalField')(default=4.99, max_digits=5, decimal_places=2)),
            ('sold', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('base', ['Product'])

        # Adding model 'Video'
        db.create_table('base_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('format', self.gf('django.db.models.fields.CharField')(default='MKV', max_length=20)),
            ('subtitle', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('subtitle_language', self.gf('django.db.models.fields.CharField')(default='English', max_length=20)),
        ))
        db.send_create_signal('base', ['Video'])

        # Adding model 'Preview'
        db.create_table('base_preview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('base', ['Preview'])

        # Adding model 'Lecturer'
        db.create_table('base_lecturer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('base', ['Lecturer'])

        # Adding model 'Series'
        db.create_table('base_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('base', ['Series'])

        # Adding model 'Poet'
        db.create_table('base_poet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_of_death', self.gf('django.db.models.fields.DateTimeField')()),
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('base', ['Poet'])

        # Adding model 'Poem'
        db.create_table('base_poem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Poet'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('copyright', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('base', ['Poem'])

        # Adding model 'Lecture'
        db.create_table('base_lecture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lecturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Lecturer'])),
            ('poem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Poem'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Video'])),
            ('preview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Preview'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Product'])),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Series'])),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('transcript', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('base', ['Lecture'])

        # Adding model 'Testimonial'
        db.create_table('base_testimonial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(default='T', max_length=1)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('published_work', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('published_worl_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('credentials', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('base', ['Testimonial'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('base_product')

        # Deleting model 'Video'
        db.delete_table('base_video')

        # Deleting model 'Preview'
        db.delete_table('base_preview')

        # Deleting model 'Lecturer'
        db.delete_table('base_lecturer')

        # Deleting model 'Series'
        db.delete_table('base_series')

        # Deleting model 'Poet'
        db.delete_table('base_poet')

        # Deleting model 'Poem'
        db.delete_table('base_poem')

        # Deleting model 'Lecture'
        db.delete_table('base_lecture')

        # Deleting model 'Testimonial'
        db.delete_table('base_testimonial')


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
        'base.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Lecturer']"}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Poem']"}),
            'preview': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Preview']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Product']"}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Series']"}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'transcript': ('django.db.models.fields.TextField', [], {}),
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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'base.poet': {
            'Meta': {'object_name': 'Poet'},
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_death': ('django.db.models.fields.DateTimeField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'base.preview': {
            'Meta': {'object_name': 'Preview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'base.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'credentials': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'profession': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '1'}),
            'published_work': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published_worl_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'base.video': {
            'Meta': {'object_name': 'Video'},
            'duration': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'MKV'", 'max_length': '20'}),
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