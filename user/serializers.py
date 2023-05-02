from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This field must be unique."
            )
        ]
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
        ]

        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data: dict) -> User:
            if validated_data["type_user"]:
                return User.objects.create_superuser(**validated_data)
            return User.objects.create_user(**validated_data)

        def to_representation(self, validated_data):
            password = validated_data.pop("password", None)
            instance = self.Meta.model(**validated_data, is_superuser=True)

            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
            