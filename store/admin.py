from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image', 'product_name', 'slug', 'harga',
                    'harga_discount', 'in_stock', 'created', 
                    'updated', 'category',]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['harga', 'harga_discount', 'in_stock']
    prepopulated_fields = {'slug': ('product_name',)}
