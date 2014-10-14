# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('production.ping.views',
                       url(r'^initializeTests/$', 'initializeTests', name='ping'),
                       url(r'^add/$', 'add', name='ping'),
                       url(r'^addProduct/(\d+)/(\d+)/(\d+)/$', 'addProduct', name='ping'),
                       url(r'^delete/(\d+)/$', 'delete', name='ping'),
                       url(r'^deleteProduct/(\d+)/(\d+)/$', 'deleteProduct', name='ping'),
                       url(r'', 'list', name='ping'),
                       )
