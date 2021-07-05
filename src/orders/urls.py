from django.urls import path

from orders import views as orders_views

app_name = 'orders'

urlpatterns = [
    path('create-order/', orders_views.CreateOrder.as_view(), name='create-order'),
    path('order-complete/', orders_views.order_complete, name='order-complete'),
]