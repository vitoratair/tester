from django.contrib import admin
from models import Product, TypeProduct


class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'site', 'typeProduct', 'accessMethod')


class TypeProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)