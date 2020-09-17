from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from webapp.forms import SimpleSearchForm
from webapp.models import Order, Basket, ProductOrder, Product


class OrderCreate(View):

    def post(self, *args, **kwargs):
        user_name = self.request.POST.get('user_name')
        address = self.request.POST.get('address')
        telephone = self.request.POST.get('telephone')
        order = Order.objects.create(user_name=user_name, address=address, telephone=telephone)
        order.save()
        for basket in Basket.objects.all():
            ProductOrder.objects.create(product_id=basket.product_id, order_id=order.pk, amount=basket.amount)
            product = Product.objects.get(pk=basket.product_id)
            print(product)
            product.amount -= basket.amount
            print(product)
            product.save()
            order.save()
        Basket.objects.all().delete()
        return redirect('products')

