# coding: utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Ping(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(_(u'Ping Name'), max_length=100, unique=True)
    description = models.CharField(
        _(u'Ping description'), max_length=300, blank=True, null=True)
    ipOrigin = models.IPAddressField(_(u'IP Origin'),
                                     blank=True, null=True,
                                     help_text='Origin IP address, without it, origin IP will be the local ip')
    ipDestination = models.IPAddressField(_(u'IP Destination'), null=True,
                                          help_text='Destination IP address')

    interval = models.IntegerField(_(u'Interval'), null=True, blank=True)
    packetNumber = models.IntegerField(
        _(u'Packet Number'), null=True, blank=True)
    setByUser = models.CharField(_(u'Made by User'), max_length=200, null=True,
                                 blank=True, help_text='Comment all made by user')

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Ping Test')
        verbose_name_plural = _(u'Ping Tests')

    def __unicode__(self):
        return self.name


class Test(models.Model):

    options = (
        ('0', 'Approved into the test'),
        ('1', 'Failed into the test'),
    )

    product = models.ForeignKey('product.Product', related_name='product_tests')
    data = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey('Ping')
    result = models.CharField(
        _(u'Expected result'), max_length=10, choices=options, blank=True)

    class Meta:
        ordering = ['data']
        verbose_name = _(u'Test result')
        verbose_name_plural = _(u'Test result')


class PingProduct(models.Model):

    options = (
        ('0', 'Approved into the test'),
        ('1', 'Failed into the test'),
    )

    ping = models.ForeignKey('Ping')
    product = models.ForeignKey('product.Product')
    result = models.CharField(
        _(u'Expected result'), max_length=10, choices=options, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Product')
        verbose_name_plural = _(u'Products')
