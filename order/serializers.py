
from rest_framework import serializers
from products.serializers import ProductSerializer
from cart.serializers import CartSerializer
from cart.models import Cart
from products.models import Product
from django.shortcuts import get_object_or_404
from user.serializers import UserSerializer

from .models import Order


class OrderProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    price = serializers.FloatField(read_only=True)
    stock = serializers.IntegerField(write_only=True)
    status = serializers.CharField(write_only=True)


class OrderSerializer(serializers.ModelSerializer):
    # cart = CartSerializer(many=True)
    # products = ProductSerializer(many=True) 

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "user_id",
            "products",
            "seller",
            "createdAt",
        ]
        read_only_fields = [
            "id",
            "status",
            "user_id",
            "products",
            "seller",
            "createdAt",
        ]

    # def create(self, validated_data):
    #     return Order.objects.create(**validated_data)
    # def create(self, validated_data: dict) -> Order:
    #     cart = validated_data.get("user").cart
    #     products = cart.products_list.all()
    #     sellers = cart.seller_list.all()

    #     for seller in sellers:
    #         seller_id = seller.id
    #         create_order = Order.objects.create(**validated_data, seller_id=seller_id)
    #         create_order.products.set(products)

    #     create_order.save()
    #     user = validated_data.get("user")
    #     orders = user.orders

    #     print(orders)

    #     return orders.all()