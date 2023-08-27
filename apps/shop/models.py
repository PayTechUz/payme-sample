from django.db import models
from django.contrib.auth.models import User

from payme.models import Item
from payme.models import BaseOrder


class CustomOrderModel(BaseOrder):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # other fields...

    def __str__(self):
        formatted_number = '{:,}'.format(self.amount)
        return f"ORDER ID: {self.id} - AMOUNT: {formatted_number} UZS"


class Product(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.TextField()
