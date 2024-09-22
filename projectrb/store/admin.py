from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_number', 'manufacturer', 'price', 'stock_quantity', 'category']
    search_fields = ['name', 'part_number', 'manufacturer']
    list_filter = ['manufacturer', 'category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_date', 'shipped_date', 'status']
    list_filter = ['status', 'order_date']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_filter = ['order', 'product']
