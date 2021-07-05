from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
    ]

class CartItemsAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'cart',
        'item_price',
    ]

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItems, CartAdmin)