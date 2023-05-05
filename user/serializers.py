from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from address.models import Address

from address.serializers import AddressSerializer
from .models import RatingChoices, User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This field must be unique."
            )
        ]
    )

    type_user = serializers.ChoiceField(
        choices=RatingChoices.choices, default=RatingChoices.client
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "type_user",
            "address",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)

        is_admin = validated_data.pop("is_admin")

        if is_admin:
            return User.objects.create_superuser(**validated_data, address=address)

        return User.objects.create_user(**validated_data, address=address)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.type_user = validated_data.get("type_user", instance.type_user)
        password = validated_data.get("password", None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserAdmSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField()
