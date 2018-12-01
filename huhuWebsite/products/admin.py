from django.contrib import admin
from .models import Category, AttributeKey, AttributeValue, Product, ProductAttribute


# Register your models here.
@admin.register(Category, AttributeKey, AttributeValue)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product,ProductAttribute)
class ProductAdmin(admin.ModelAdmin):
    pass


