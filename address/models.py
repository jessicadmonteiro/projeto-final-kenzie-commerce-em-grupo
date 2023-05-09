from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=127)
    neighborhood = models.CharField(max_length=127)
    number = models.CharField(max_length=50)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
