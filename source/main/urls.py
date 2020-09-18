"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from webapp.views import ProductsView, OneProductView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, AddToBasket, BasketView, DeleteFromBasketView
from webapp.views.order import OrderCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', OneProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create_view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/add_to_basket/', AddToBasket.as_view(), name='add_to_basket'),
    path('basket/view/', BasketView.as_view(), name='basket_view'),
    path('basket/delete/<int:pk>/', DeleteFromBasketView.as_view(), name='basket_delete_view'),

    path('order/create/', OrderCreate.as_view(), name='order_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
