# coding: utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):

    name = models.CharField(_(u'Product Name'), max_length=100, unique=True)
    site = models.URLField(_(u'Product Site'))
    TypeProduct = models.ForeignKey('TypeProduct')

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')

    def __unicode__(self):
        return self.name


class TypeProduct(models.Model):

    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=45, unique=True)


    class Meta:
        ordering = ['name']
        verbose_name = _(u'Tipo de produto')
        verbose_name_plural = _(u'Tipos de produtos')

    def __unicode__(self):
        return self.name
