from django.contrib import admin
from .models import Category, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'shipped_date', 'status')
    list_filter = ('status', 'order_date')
    inlines = [OrderItemInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'manufacturer', 'price', 'stock_quantity', 'category')
    search_fields = ('name', 'part_number', 'manufacturer')
    list_filter = ('manufacturer', 'category')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
