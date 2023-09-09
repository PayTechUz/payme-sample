from django.db import models

from payme.models import Item
from payme.models import BaseOrder


class Product(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.TextField()

    def __str__(self):
        return self.items.__str__()


class CustomOrderModel(BaseOrder):
    full_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=24)
    wants_at = models.DateTimeField(null=True, blank=True)
