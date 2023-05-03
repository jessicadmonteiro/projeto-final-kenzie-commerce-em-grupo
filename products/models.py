from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(max_length=127)


# user = models.ForeignKey(
#     "users.User", on_delete=models.CASCADE, related_name="products"
# )
# cart = models.ManyToManyField(
#     "cart.Cart",
#     related_name="cart_products"
#     )
