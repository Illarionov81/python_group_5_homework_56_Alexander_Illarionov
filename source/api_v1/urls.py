from django.urls import path

from api_v1.views import product_create_view, get_token_view

app_name = 'api_v1'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('product/create/', product_create_view, name='product_create'),
]