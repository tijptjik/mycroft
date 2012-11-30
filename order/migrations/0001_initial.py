# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UnawareOrder'
        db.create_table('order_unawareorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3)),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True)),
        ))
        db.send_create_signal('order', ['UnawareOrder'])

        # Adding model 'Item'
        db.create_table('order_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.UnawareOrder'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal('order', ['Item'])


    def backwards(self, orm):
        # Deleting model 'UnawareOrder'
        db.delete_table('order_unawareorder')

        # Deleting model 'Item'
        db.delete_table('order_item')


    models = {
        'order.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.UnawareOrder']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'order.unawareorder': {
            'Meta': {'object_name': 'UnawareOrder'},
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'})
        }
    }

    complete_apps = ['order']