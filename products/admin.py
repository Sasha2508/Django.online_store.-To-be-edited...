from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'product_brand',
        'year_of_manufacture',
        'color',
        'quantity',
        'product_image',
        'size',
        'weight',
        'description'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description'
    ]



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'category'
    ]