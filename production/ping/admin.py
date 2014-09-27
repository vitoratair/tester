from django.contrib import admin
from production.ping.models import Ping

class PingAdmin(admin.ModelAdmin):
	list_display = ('id', 'description')


admin.site.register(Ping, PingAdmin)
