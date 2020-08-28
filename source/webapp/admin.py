from django.contrib import admin
from webapp.models import Product, Basket


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('pk', 'name', 'amount', 'price')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


class BasketAdmin(admin.ModelAdmin):
    list_filter = ('amount',)
    list_display = ('pk', 'amount')
    list_display_links = ('pk', 'amount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
