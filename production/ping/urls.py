# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('production.ping.views',
    url(r'^deleteProduct/(\d+)/(\d+)/$', 'deleteProduct', name='ping'),
    url(r'', 'list', name='ping'),
)
