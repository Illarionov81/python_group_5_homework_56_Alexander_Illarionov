from django.contrib import admin

from webapp.forms import OrderForm
from webapp.models import Product, Basket, Order, ProductOrder


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('pk', 'name', 'amount', 'price')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


class BasketAdmin(admin.ModelAdmin):
    list_filter = ('amount',)
    list_display = ('pk', 'amount',)
    list_display_links = ('pk', 'amount',)


class ProductOrderInLine(admin.TabularInline):
    model = ProductOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderInLine,)
    list_filter = ('user_name',)
    list_display = ('pk', 'user_name', 'telephone', 'address', 'created_time')
    list_display_links = ('pk', 'user_name',)
    ordering = ('-created_time',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)
