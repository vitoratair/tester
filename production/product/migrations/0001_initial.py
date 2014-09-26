# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'product_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('TypeProduct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.TypeProduct'])),
        ))
        db.send_create_signal(u'product', ['Product'])

        # Adding model 'TypeProduct'
        db.create_table(u'product_typeproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
        ))
        db.send_create_signal(u'product', ['TypeProduct'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'product_product')

        # Deleting model 'TypeProduct'
        db.delete_table(u'product_typeproduct')


    models = {
        u'product.product': {
            'Meta': {'ordering': "['id']", 'object_name': 'Product'},
            'TypeProduct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.TypeProduct']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'product.typeproduct': {
            'Meta': {'ordering': "['name']", 'object_name': 'TypeProduct'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        }
    }

    complete_apps = ['product']