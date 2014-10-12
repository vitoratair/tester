# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('production.login.views',
                       url(r'^logout/$', 'logout', name='login'),
                       url(r'^validate/$', 'validate', name='login'),
                       url(r'^$', 'home', name='login'),
                       )
