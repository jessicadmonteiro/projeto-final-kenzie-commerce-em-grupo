from django.db import models
from user.models import User
from products.models import Product

class Cart(models.Model):
    products_list = models.ManyToManyField(Product, related_name="products")
    seller_list = models.ManyToManyField(User, related_name="cart_list")
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="cart", null=True)
