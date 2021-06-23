from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from users.forms import UserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.

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
               
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #Check if user enter secret world to become a shop manager
            for u in Profile.objects.filter(user_details__contains='Manager'):
                u.sale_staff = True
                u.save()
                # group = Group.objects.get(name='Manager')
                # u.groups.add(group)
                # u.save()
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form': profile_form,
        
    }
    return render(request, 'users/profile.html', context=context)