import django
from django.contrib.auth.models import User

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, DetailView, RedirectView
from django.urls import reverse_lazy
from . import models
from books import models as book_models

# Create your views here.

class CartView(DetailView):
    template_name='carts/cart-detail.html'
    model = models.Cart

    def get_object(self, queryset=None):
        #get cart
        if self.request.user.is_authenticated:
            customer = self.request.user
            print(customer)
            cart_id = self.request.session.get('cart_id')
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={
                    'customer':customer
                },
            )
        else:
            cart_id = self.request.session.get('cart_id')
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={
                },
            )    
        if created:
            self.request.session['cart_id'] = cart.pk
        
       
        #get book id
        book_id = self.request.GET.get('book_id')
        
        if book_id:
            book = book_models.Book.objects.get(pk=int(book_id))
            item_price = book_models.Book.objects.get(pk=int(book_id)).book_price
            item_in_cart, book_created = models.CartItems.objects.get_or_create(
                cart=cart,
                book=book,
                defaults={
                    'item_price': item_price
                },
            )
            if not book_created:
                q = item_in_cart.quantity + 1
                item_in_cart.quantity = q
                item_in_cart.save()
             
        
        return cart


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cart_items'] = models.CartItems.objects.all()
    #     return context

class DeleteCartItem(RedirectView):
    model = models.CartItems
    success_url = reverse_lazy('carts:cart_detail')

    def get_redirect_url(self, *args, **kwargs):
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class UpdateCartView(View):
    def post(self, request):
        action = request.POST.get('submit')
        cart_id = self.request.session.get('cart_id')
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk

        items = cart.cart_items.all()
        if items:
            for key, value in request.POST.items():
                if 'item-quantity_' in key:
                    pk=int(key.split('_')[1])
                    item = items.get(pk=pk)
                    item.quantity = int(value)
                    item.save()
        if action == 'save-cart':        
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
        elif action == 'create-order':
            return HttpResponseRedirect(reverse_lazy('orders:create-order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
