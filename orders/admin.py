from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'date',
        'payment_method',
        'delivery_method',
        'delivery_date',
        'total_price'
    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'date',
        'item_price',
        'quantity',
        'sub_total',
        'product'
    ]