from django.db import models


class ProductStatus(models.TextChoices):
    disponivel = "disponivel"
    indisponivel = "indisponivel"


class Product(models.Model):
    name = models.CharField(max_length=127, unique=True)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(
        max_length=127, choices=ProductStatus.choices, default=ProductStatus.disponivel
    )

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="products"
    )

    cart = models.ManyToManyField("cart.Cart", related_name="cart_products")
