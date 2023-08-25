from django.db import models

from payme.models import BaseOrder


class CustomOrderModel(BaseOrder):
    user_id = models.IntegerField(null=True, blank=True) # other fields...

    def __str__(self):
        return f"ORDER ID: {self.id} - AMOUNT: {self.amount}"
