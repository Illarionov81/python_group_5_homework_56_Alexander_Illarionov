from django import forms
from webapp.models import Product
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {'category': forms.widgets.CheckboxSelectMultiple}
