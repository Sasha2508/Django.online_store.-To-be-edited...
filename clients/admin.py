from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'login',
        'email',
        'password',
        'address_1',
        'address_2',
        'city',
        'state_or_province',
        'county',
        'postal_code'
    ]

