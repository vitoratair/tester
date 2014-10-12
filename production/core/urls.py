# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('production.core.views',
                       url(r'^setDefaultProduct/$', 'setDefaultProduct', name='core'),
                       url(r'^testStatus/$', 'testStatus', name='core'),
                       url(r'', 'home', name='core'),
                       )
