from django.db import models
from user.models import User
from products.models import Product


class Cart(models.Model):
    products_list = models.ManyToManyField(
        Product, blank=True, related_name="products_cart"
    )
    seller_list = models.IntegerField()
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
