from django.db.models import Count, Sum, FloatField, F
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist

from webapp.forms import BasketForm
from webapp.models import Product, Basket


class AddToBasket(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        try:
            basket = Basket.objects.get(product=product)
            if product.amount > 0:
                if basket.amount < product.amount:
                    basket.amount += 1
                    basket.save()
                else:
                    basket.amount = product.amount
                    basket.save()
        except ObjectDoesNotExist:
            basket = Basket.objects.create(product=product)
            basket.amount = 1
            basket.save()
        print(basket)
        return redirect('products')


class BasketView(ListView):
    template_name = 'basket/basket_view.html'
    model = Basket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = []
        for i in Basket.objects.all():
            baskets.append({'total': i.product.price * i.amount, 'product': i.product, 'amount': i.amount, 'pk': i.pk})
        context['baskets'] = baskets
        total = 0
        for i in Basket.objects.all():
            total += i.product.price * i.amount
        context['total'] = total
        return context



