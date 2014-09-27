# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('production.core.views',
	url(r'^setDefaultProduct/$', 'setDefaultProduct', name='core'),
	url(r'^testBoard/$', 'testBoard', name='core'),
	url(r'^testStatus/$', 'testStatus', name='core'),
    url(r'', 'home', name='core'),
)
