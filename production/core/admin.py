from django.contrib import admin
from production.core.models import Information


class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'machine', 'interface')


admin.site.register(Information, InformationAdmin)
