import uuid
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Address(models.Model):
    street = models.CharField(max_length=127)
    neighborhood = models.CharField(max_length=127)
    number = models.CharField(max_length=50)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(validators=[MinLengthValidator(8), MaxLengthValidator(8)])
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, related_name="address")
