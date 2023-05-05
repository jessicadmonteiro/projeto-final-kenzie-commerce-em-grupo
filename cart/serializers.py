from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = [
            "products_list",
            "seller_list",
            "total",
        ]
        extra_kwargs = {"seller_list": {"many": True}}