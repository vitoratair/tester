from django.contrib import admin
from models import Login, Perfil

class LoginAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'username', 'perfil')

admin.site.register(Login, LoginAdmin)

class PerfilAdmin(admin.ModelAdmin):
	list_display = ('id', 'perfil', 'description')

admin.site.register(Perfil, PerfilAdmin)