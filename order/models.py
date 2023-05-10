from django.db import models
from products.models import Product
from user.models import User

# Create your models here.


class StatusChoides(models.TextChoices):
    realizado = "realizado"
    andamento = "andamento"
    entregue = "entregue"


class Order(models.Model):
    status = models.CharField(max_length=30, default=StatusChoides.realizado)
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="seller_orders",
    )
    products = models.ManyToManyField(Product, related_name="orders")
