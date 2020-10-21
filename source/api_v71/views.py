from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from webapp.models import Product, Order
from api_v71.serializers import ProductSerializer, OrderSerializer


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(ViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAdminUser()]
        return super().get_permissions()

    def list(self, request):
        products = Product.objects.all()
        srl = ProductSerializer(products, many=True, context={'request': request})
        return Response(srl.data)

    def create(self, request):
        srl = ProductSerializer(data=request.data, context={'request': request})
        if srl.is_valid():
            product = srl.save()
            return Response(srl.data)
        else:
            return Response(srl.errors, status=400)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        srl = ProductSerializer(product)
        return Response(srl.data)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        srl = ProductSerializer(data=request.data, instance=product, context={'request': request})
        if srl.is_valid():
            product = srl.save()
            return Response(srl.data)
        else:
            return Response(srl.errors, status=400)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'pk': pk})



# class OrderViewSet(viewsets.ModelViewSet):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer


class OrderViewSet(ViewSet):
    queryset = Order.objects.all()

    def list(self, request):
        orders = Order.objects.all()
        srl = OrderSerializer(orders, many=True, context={'request': request})
        return Response(srl.data)

    def create(self, request):
        srl = OrderSerializer(data=request.data, context={'request': request})
        if srl.is_valid():
            order = srl.save()
            return Response(srl.data)
        else:
            return Response(srl.errors, status=400)

    def retrieve(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        srl = OrderSerializer(order, context={'request': request})
        return Response(srl.data)
