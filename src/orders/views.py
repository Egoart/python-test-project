from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import FormView
from . import models, forms
from carts.models import Cart
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.

def order_complete(request):
    return render(request, 'orders/completed-order.html')


class CreateOrder(FormView):
    form_class = forms.OrderForm
    template_name ='orders/create-order.html'

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
        ci = form.cleaned_data.get('contact_info')
        order = models.Order.objects.create(
            cart=cart,
            contact_info= ci
        )
        del self.request.session['cart_id']
        return HttpResponseRedirect(reverse_lazy('orders:order-complete'))
        
    def get_initial(self):
        initial_data = super().get_initial()

        if self.request.user.is_authenticated:
            user_phone = self.request.user.profile.phone
            initial_data['contact_info'] = user_phone
        else:
            initial_data['contact_info'] = ''   
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        context['object'] = cart
        return context