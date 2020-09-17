from django.db.models import Count, Sum, FloatField, F
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist

from webapp.forms import BasketForm, OrderForm
from webapp.models import Product, Basket


class AddToBasket(View):

    def post(self, request, *args, **kwargs):
        from_url = request.META.get('HTTP_REFERER', 'products')
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        amount = request.POST.get('amount')
        print(from_url)
        if amount:
            amount = int(amount)
            if amount < 0:
                amount = amount * (-1)
        else:
            amount = 1
        try:
            basket = Basket.objects.get(product=product)
            if product.amount > 0:
                if basket.amount + amount < product.amount:
                    basket.amount += amount
                    basket.save()
                else:
                    basket.amount = product.amount
                    basket.save()
        except ObjectDoesNotExist:
            basket = Basket.objects.create(product=product)
            if amount < product.amount:
                basket.amount = amount
                basket.save()
            else:
                basket.amount = product.amount
                basket.save()
        return redirect(from_url)


class BasketView(ListView):
    template_name = 'basket/basket_view.html'
    model = Basket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = []
        for i in Basket.objects.all():
            baskets.append({'total': i.product.price * i.amount,
                            'product': i.product, 'amount': i.amount, 'pk': i.pk})
        context['baskets'] = baskets
        total = 0
        for i in Basket.objects.all():
            total += i.product.price * i.amount
        context['total'] = total
        return context


class DeleteFromBasketView(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        basket = Basket.objects.get(product=product)
        amount = self.request.POST.get('delete')
        print(amount)
        if amount:
            amount = int(amount)
            if amount < 0:
                amount = amount * (-1)
            if basket.amount > amount:
                basket.amount -= amount
                basket.save()
            else:
                basket.delete()
        return redirect('basket_view')




