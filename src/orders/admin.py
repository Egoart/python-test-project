from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display =[
        'pk',
        'cart',
        'order_status',
        'contact_info',
        'order_created',
        
    ]

admin.site.register(models.Order, OrderAdmin)
