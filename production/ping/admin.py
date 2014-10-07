from django.contrib import admin
from production.ping.models import Ping, PingProduct, Test


class PingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',
                    'ipOrigin', 'ipDestination', 'interval',
                    'packetNumber', 'setByUser')


class PingProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'ping', 'result')


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'test', 'result')

admin.site.register(Ping, PingAdmin)
admin.site.register(PingProduct, PingProductAdmin)
admin.site.register(Test, TestAdmin)
