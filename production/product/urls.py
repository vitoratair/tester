# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('production.product.views',
    url(r'^list/$', 'list', name='product'),
)
