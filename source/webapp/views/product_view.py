from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import SimpleSearchForm, ProductForm
from webapp.models import Product


def multi_delete(request):
    data = request.POST.getlist('id')
    Product.objects.filter(pk__in=data).delete()
    return redirect('projects')


class ProductsView(ListView):
    template_name = 'product/products_view.html'
    context_object_name = 'products_list'
    model = Product
    form = SimpleSearchForm
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = self.model.objects.filter(amount__gte=1)
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return data.order_by('category', 'name')


class OneProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


