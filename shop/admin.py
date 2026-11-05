from django.contrib import admin

from shop.models import Category, Order, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
