from django.contrib import admin

from shop.models import Product
from shop.models import CustomOrderModel


admin.site.register(Product)
admin.site.register(CustomOrderModel)
