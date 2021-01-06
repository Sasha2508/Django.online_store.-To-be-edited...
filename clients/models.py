from django.db import models

class Client(models.Model):
    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(blank=False, null=False, max_length=30, verbose_name='First Name')
    last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
    login = models.CharField(blank=False, null=False, max_length=30, verbose_name='Login')
    email = models.EmailField(blank=False, null=False, max_length=80, verbose_name='Email Address')
    password = models.CharField(blank=False, null=False, max_length=30, verbose_name='Password')
    address_1 = models.CharField(blank=True, null=True, max_length=60, verbose_name='Corporate Address')
    address_2 = models.CharField(blank=False, null=False, max_length=60, verbose_name='Street Address')
    city = models.CharField(blank=False, null=False, max_length=20, verbose_name='City')
    state_or_province = models.CharField(blank=False, null=False, max_length=30, verbose_name='State / Province')
    county = models.CharField(blank=True, null=False, max_length=30, verbose_name='County')
    postal_code = models.CharField(blank=False, null=False, max_length=14, verbose_name='Postal / Zip Code')




