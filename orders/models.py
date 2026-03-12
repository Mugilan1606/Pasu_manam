from django.db import models

class Order(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    product = models.CharField(max_length=100)

    quantity = models.IntegerField()

    total = models.IntegerField()

    payment = models.CharField(max_length=20)

    date = models.DateTimeField(auto_now_add=True)
