from django.contrib import admin
from production.ping.models import Ping


class PingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'ipOrigin',
                    'ipDestination', 'interval', 'packetNumber', 'setByUser', 'result')


admin.site.register(Ping, PingAdmin)