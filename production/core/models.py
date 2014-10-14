# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Information(models.Model):

    machine = models.CharField(_(u'Machine name'), max_length=100, unique=True)
    interface = models.CharField(_(u'Interface Name'), max_length=30)

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Machine Information')
        verbose_name_plural = _(u'Machine Informations')

    def __unicode__(self):
        return self.machine
