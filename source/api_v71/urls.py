from django.urls import path

from api_v1.views import get_token_view

app_name = 'api_v1'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
]