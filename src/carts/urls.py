from django.urls import path

from carts import views as carts_views

app_name = 'carts'

urlpatterns = [
    path('', carts_views.CartView.as_view(), name='cart_detail'),
    path('delete-cart-item/<int:pk>', carts_views.DeleteCartItem.as_view(), name='delete-cart-item'),
    path('update-cart/', carts_views.UpdateCartView.as_view(), name='update-cart'),
]