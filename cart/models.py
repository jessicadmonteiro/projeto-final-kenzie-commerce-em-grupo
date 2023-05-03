from django.db import models


class Cart(models.Model):
    products_list = models.CharField()
    seller_list = models.CharField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, related_name="cart")
