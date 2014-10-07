# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('production.product.views',
                       url(r'^delete/(\d+)/$', 'delete', name='product'),
                       url(r'^showTest/(\d+)/$', 'showTest', name='product'),
                       url(r'^getTest/(\d+)/$', 'getTest', name='product'),
                       url(r'^list/$', 'list', name='product'),
                       )
