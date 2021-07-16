from django.contrib.auth.forms import PasswordChangeForm
from django.http.response import Http404
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from users.forms import UserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from carts.models import Cart
from orders.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

# Create your views here.
#restrict access to Cart page
class CartItemsDetail(LoginRequiredMixin, DetailView):
    model = Cart
    template_name='users/user_cart_ordered.html'    

    def get_object(self, queryset=None):
        obj = super(CartItemsDetail, self).get_object(queryset=queryset)
        if obj.customer != self.request.user:
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = int(self.kwargs.get('pk'))
        context['order_detail'] = Order.objects.get(cart=cart_id)
        return context

class ModifyPassword(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('users:password-success')

def password_success(request):
    return render(request, 'users/password_success.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.post_index = form.cleaned_data.get('post_index')
            user.profile.address1 = form.cleaned_data.get('address1')
            user.profile.address2 = form.cleaned_data.get('address2')
            cgroup = Group.objects.get(name='Customer')
            user.groups.add(cgroup) 
            user.save()        
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
            
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    customer = request.user           
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #Check if user enter secret world to become a shop manager
            personel = Profile.objects.filter(user_details__contains='Manager')
            if personel:
                for u in personel:
                    u.sale_staff = True
                    mgroup = Group.objects.get(name='Manager')
                    cgroup = Group.objects.get(name='Customer')
                    customer.groups.add(mgroup)
                    customer.groups.remove(cgroup)
                    u.save()
            

            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_orders = Order.objects.filter(cart__customer=customer)

    context = {
        'user_form' : user_form,
        'profile_form': profile_form,
        'user_orders': user_orders,
    }
    return render(request, 'users/profile.html', context=context)

#Info page for those who wants to be a manager
def info_become_manager(request):
    return render(request, 'users/become_manager.html')
