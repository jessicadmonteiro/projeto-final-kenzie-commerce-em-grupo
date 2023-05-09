from rest_framework import serializers
from .models import Order


class OrderProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    price = serializers.FloatField(read_only=True)
    stock = serializers.IntegerField(write_only=True)
    status = serializers.CharField(write_only=True)


class OrderSerializer(serializers.ModelSerializer):
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
