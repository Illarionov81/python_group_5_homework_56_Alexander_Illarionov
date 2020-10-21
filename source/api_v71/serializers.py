from rest_framework import serializers
from webapp.models import Product, Order, ProductOrder, Basket


# class BasketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'amount', 'price']


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('id', 'order', 'product', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    order_product = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_name', 'telephone', 'address', 'created_time', 'user', 'order_product']


