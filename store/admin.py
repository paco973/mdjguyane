from django.contrib import admin
from .models import Category, Product, CartItem, Cart, CategoryStock

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(CategoryStock)