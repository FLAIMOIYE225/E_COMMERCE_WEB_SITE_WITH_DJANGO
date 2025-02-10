from django.contrib import admin
from .models import Product, Category, Order, Cart


# Admin classe
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'thumbnail', 'date', 'category')
    #fields = ('name', 'price', 'thumbnail')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered', 'id', 'product', 'quantity', 'status')
    #list_display = ('user', 'product', 'quantity', 'orderAccepted', 'orderNotAborted', 'orderPackaging', 'orderDelivered', 'orderDate')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)