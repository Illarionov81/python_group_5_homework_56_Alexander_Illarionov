from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
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

        user = self.request.user
        print(user)
        if user != AnonymousUser:
            order = Order.objects.create(user_name=user_name, address=address, telephone=telephone, user_id=user.pk)
            order.save()
        else:
            order = Order.objects.create(user_name=user_name, address=address, telephone=telephone)
            order.save()
        for basket in Basket.objects.all():
            ProductOrder.objects.create(product_id=basket.product_id, order_id=order.pk, amount=basket.amount)
            product = Product.objects.get(pk=basket.product_id)
            product.amount -= basket.amount
            product.save()
            order.save()
        Basket.objects.all().delete()
        return redirect('products')


class OrderView(LoginRequiredMixin, ListView):
    template_name = 'order/order_view.html'
    context_object_name = 'orders'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        products = []
        orders = Order.objects.filter(user_id=self.request.user.pk)
        for order in orders.values_list('pk'):
            for i in ProductOrder.objects.filter(order_id=order):
                products.append({'total': i.product.price * i.amount,
                                'product': i.product, 'amount': i.amount, 'pk': i.pk})
                context['products'] = products
                total += i.product.price * i.amount
        context['total'] = total
        return context


