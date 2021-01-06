from django.db import models
from django.db import models

class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')
    price = models.FloatField(blank=False, null=False, verbose_name='Price')



    product_brand = models.CharField(blank=False, null=False, max_length=200, verbose_name='Product_Brand', default='Not Specified')
    year_of_manufacture = models.IntegerField(blank=False, null=True, verbose_name='Year_Of_Manufacture')
    color = models.CharField(blank=False, null=False, max_length=50, verbose_name='Color', default='Not specified')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Quantity', default=1)
    product_image = models.ImageField(blank=False, null=False, verbose_name='Product_Image', default='No image available')
    size = models.CharField(blank=False, null=False, max_length=100, verbose_name='Size', default='Small')
    weight = models.DecimalField(blank=False, null=False, decimal_places=3, max_digits=12, verbose_name='Weight', default='180.00')
    description = models.CharField(blank=False, null=False, max_length=300, verbose_name='Description', default='Not Specified')

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(blank=False, null=False, max_length=200, verbose_name='Title')
    description = models.CharField(blank=False, null=False, max_length=300, verbose_name='Description', default='Not Specified')


class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)