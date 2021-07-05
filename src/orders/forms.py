from django.forms import ModelForm
from .models import Order



class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['cart', 'order_status', 'order_created', 'order_modified']
    

        

