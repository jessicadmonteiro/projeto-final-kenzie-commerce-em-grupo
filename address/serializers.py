from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id"
            "street"
            "neighborhood"
            "number"
            "city"
            "state"
            "zipcode"
        ]
        