from django.contrib import admin
from .models import Product, Order

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'product', 'quantity', 'total_price', 'date']
    
