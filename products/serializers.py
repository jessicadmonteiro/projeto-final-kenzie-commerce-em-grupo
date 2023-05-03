from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "category", "price", "stock", "status"]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
