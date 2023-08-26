from django.db import models

from payme.models import BaseOrder


class CustomOrderModel(BaseOrder):
    user_id = models.IntegerField(null=True, blank=True)  # other fields...
