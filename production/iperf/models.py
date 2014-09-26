# coding: utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Iperf(models.Model):

    description = models.CharField(_(u'Iperf Description'), max_length=1000, unique=True)
    ipOrigin =models.IPAddressField(_(u'Origin IP'))
    ipDestination =models.IPAddressField(_(u'Destination IP'))

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Iperf test')
        verbose_name_plural = _(u'Iperf tests')

    def __unicode__(self):
        return self.description

