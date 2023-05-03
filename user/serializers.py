from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import RatingChoices, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
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
            # "is_admin"
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        is_admin = validated_data.pop("is_admin")
        if is_admin:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

class UserAdmSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField()