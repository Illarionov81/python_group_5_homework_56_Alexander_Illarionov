from django import forms
from webapp.models import Product, Basket, Order
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {'category': forms.widgets.Select}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['amount']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'address', 'telephone', 'product',]
