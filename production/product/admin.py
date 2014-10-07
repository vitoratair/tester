from django.contrib import admin
from models import Product, TypeProduct, Test


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'typeProduct',
                    'accessMethod', 'default', 'get_test')


class TypeProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(Test, TestAdmin)
