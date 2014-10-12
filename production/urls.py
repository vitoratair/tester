from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ping/', include('production.ping.urls', namespace='ping')),
                       url(r'^core/', include('production.core.urls', namespace='core')),
                       url(r'^product/', include('production.product.urls', namespace='cproductore')),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'', include('production.login.urls', namespace='login')),
                       )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
