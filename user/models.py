from django.db import models
from django.contrib.auth.models import AbstractUser

class RatingChoices(models.TextChoices):
    seller = "seller",
    client = "client"



class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    type_user = models.CharField(max_length=20, blank=True, default=RatingChoices.client)
