from api_v1.views import get_token_view
from django.urls import include, path
from rest_framework import routers
from api_v71 import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)

app_name = 'api_v2'

urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', get_token_view, name='get_token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

