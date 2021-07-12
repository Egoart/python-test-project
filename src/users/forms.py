from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile


class UserForm(UserCreationForm):
    phone = forms.CharField(
        max_length=12,
        label='Номер телефона'
    )
    country = forms.CharField(
        max_length=100,
        label='Страна'
    )
    city = forms.CharField(
        max_length=100,
        label='Город'
    )
    post_index = forms.IntegerField(
        label='Индекс'
    )
    address1 = forms.CharField(
        max_length=200,
        label='Адрес 1'
    )
    address2 = forms.CharField(
        max_length=200,
        label='Адрес 2'
    )
    class Meta:
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            'email', 
            'first_name', 
            'last_name', 
            'phone', 
            'country', 
            'city', 
            'post_index', 
            'address1', 
            'address2'
        ]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=12,
        label='Номер телефона'
    )
    user_details = forms.CharField(
        max_length=1000,
        label='Дополнительно'
    )
    class Meta:
        model = Profile
        fields = [ 
            'first_name', 
            'last_name', 
            'phone', 
            'user_details'
        ]

    