# coding: utf-8
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Ping(models.Model):


	name = models.CharField(_(u'Ping Name'), max_length=100, unique=True)
	description = models.CharField(_(u'Ping description'), max_length=300, blank=True)
	ipOrigin = models.IPAddressField(_(u'IP Origin'))
	ipDestination = models.IPAddressField(_(u'IP Destination'))
	interval = models.IntegerField(_(u'Interval'), blank=True)
	packetNumber = models.IntegerField(_(u'Packet Number'))


	class Meta:
		ordering = ['id']
		verbose_name = _(u'Ping Test')
		verbose_name_plural = _(u'Ping Tests')

	def __unicode__(self):
		return self.name