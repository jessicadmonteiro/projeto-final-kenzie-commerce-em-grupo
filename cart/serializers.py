from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    products_list = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            "products_list",
            "seller_list",
            "total",
        ]
