from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product, ProductStatus
from user.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        name = serializers.CharField(
            validators=[
                UniqueValidator(
                    queryset=Product.objects.all(), message="This field must be unique."
                )
            ]
        )
        status = serializers.ChoiceField(choices=ProductStatus, required=False)

        model = Product
        fields = ["id", "name", "category", "price", "stock", "status"]

    def create(self, validated_data):
        if validated_data["stock"] == 0:
            validated_data["status"] = "indisponivel"
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if instance.stock == 0:
            instance.status = "indisponivel"
        else:
            instance.status = "disponivel"

        instance.save()
        return instance
