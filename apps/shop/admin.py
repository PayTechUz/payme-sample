from django.contrib import admin
from unfold.admin import ModelAdmin

from shop.models import CustomOrderModel


@admin.register(CustomOrderModel)
class CustomOrderModelAdmin(ModelAdmin):
    # The fields to display on objects list in the admin panel
    list_display = ("id", "amount",)

    # The fields of CustomOrderModel which used to add or update objects in the admin panel
    fields = ("amount",)

    # The fields which used to sort objects
    ordering = ("-amount",)

    # The fields to search through objects
    search_fields = ("id", "amount",)

    # all configurations here:
    # https://github.com/unfoldadmin/django-unfold?tab=readme-ov-file#available-unfoldadminmodeladmin-options
