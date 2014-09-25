from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class Login(models.Model):
    email = models.EmailField(_('E-mail'), blank=True)
    password = models.CharField(_('Password'), max_length=8)
    username = models.CharField(_('User name'), max_length=20, unique=True)
    perfil = models.ForeignKey('Perfil', default='2')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Perfil(models.Model):
    perfil = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['perfil']

    def __unicode__(self):
        return self.perfil