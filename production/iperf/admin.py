from django.contrib import admin
from models import Iperf


class IperfAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', 'ipOrigin', 'ipDestination')


admin.site.register(Iperf, IperfAdmin)