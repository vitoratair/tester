# coding: utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from production.ping.models import Ping


class Product(models.Model):

    accessMethodOptions = (
        ('SSH', 'SSH communication'),
        ('CGI', 'CGI communication'),
    )

    name = models.CharField(_(u'Product Name'), max_length=100, unique=True)
    site = models.URLField(_(u'Product Site'), blank=True)
    typeProduct = models.ForeignKey('TypeProduct')
    accessMethod = models.CharField((u'Communication'),
                                    max_length=10, choices=accessMethodOptions)
    default = models.BooleanField(_(u'Default on system'))
    test = models.ManyToManyField('Test', blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')

    def get_test(self):
        return self.test.all()

    def __unicode__(self):
        return self.name


class Test(models.Model):

    name = models.CharField(max_length=45, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Teste')
        verbose_name_plural = _(u'Testes')

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
