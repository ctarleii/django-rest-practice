from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rest_app.models import Product, Category


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'category', 'price', 'discount')
    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
        }),
        ('Other options', {
            'fields': ('price', 'category', 'discount')
        })
    )


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('cat_name',)
