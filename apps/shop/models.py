from django.db import models

from payme.models import Item
from payme.models import BaseOrder


class Product(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        amount = self.items.price / 100
        formatted_number = '{:,}'.format(amount)
        return f"{self.items.title} - {formatted_number} UZS"


class CustomOrderModel(BaseOrder):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=24)
    wants_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        amount = self.amount / 100
        formatted_number = '{:,}'.format(amount)
        return f"ORDER ID: {self.id} - AMOUNT: {formatted_number} UZS"
