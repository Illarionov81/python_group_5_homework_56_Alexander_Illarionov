from django.contrib.sessions.models import Session
from django.db.models import Count, Sum, FloatField, F
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist

from webapp.forms import BasketForm, OrderForm
from webapp.models import Product, Basket
from django.contrib import messages



class AddToBasket(View):

    def post(self, request, *args, **kwargs):
        if not self.request.session.session_key:
            self.request.session.save()
        session = Session.objects.get(session_key=self.request.session.session_key)
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
            basket = Basket.objects.get(product=product, session_id=session.session_key)
            if product.amount > 0:
                if basket.amount + amount < product.amount:
                    basket.amount += amount
                    basket.session_id = session.pk
                    basket.save()
                    messages.add_message(self.request, messages.SUCCESS, 'Товар успешно добавлен в корзину!'
                                                                         ' Добавленно %s шт.' % amount)
                else:
                    add = product.amount - basket.amount
                    basket.amount = product.amount
                    basket.session_id = session.pk
                    basket.save()
                    if add > 0:
                        messages.add_message(self.request, messages.WARNING, 'К сожалению это последний '
                                                                            ' товар на складе! Добавленно '
                                                                           '%s шт.' % add)
                    else:
                        messages.add_message(self.request, messages.ERROR, 'К сожалению это последний '
                                                                             ' товар на складе! Добавленно '
                                                                             '%s шт.' % add)

        except ObjectDoesNotExist:
            basket = Basket.objects.create(product=product, session_id=session.session_key)
            if amount < product.amount:
                basket.amount = amount
                basket.session_id = session.pk
                basket.save()
                messages.add_message(self.request, messages.SUCCESS, 'Товар успешно добавлен в корзину!'
                                                                     ' Добавленно %s шт.' % amount)
            else:
                add = product.amount
                basket.amount = product.amount
                basket.session_id = session.pk
                basket.save()
                messages.add_message(self.request, messages.ERROR, 'К сожалению это последний '
                                                                     ' товар на складе! Добавленно %s шт.' % add)
        session.save()
        return redirect(from_url)


class BasketView(ListView):
    template_name = 'basket/basket_view.html'
    model = Basket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = []
        for i in Basket.objects.filter(session_id=self.request.session.session_key):
            baskets.append({'total': i.product.price * i.amount,
                            'product': i.product, 'amount': i.amount, 'pk': i.pk})
        context['baskets'] = baskets
        total = 0
        for i in Basket.objects.filter(session_id=self.request.session.session_key):
            total += i.product.price * i.amount
        context['total'] = total
        return context


class DeleteFromBasketView(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        basket = Basket.objects.get(product=product)
        context = {'basket': basket}
        amount = self.request.POST.get('delete')
        print(amount)
        if amount:
            amount = int(amount)
            if amount < 0:
                amount = amount * (-1)
            if basket.amount > amount:
                basket.amount -= amount
                basket.save()
                messages.add_message(self.request, messages.WARNING, 'Количество товара уменьшенно на %s шт.' % amount)
            else:
                basket.delete()
                messages.add_message(self.request, messages.WARNING, 'Товар успешно удален из корзины!'
                                                                     ' В количестве %s шт.' % basket.amount)
        else:
            messages.add_message(self.request, messages.ERROR, 'Что то пошло не так!'
                                                               ' Возможно Вы забыли указать количество.')
        return redirect('basket_view')




