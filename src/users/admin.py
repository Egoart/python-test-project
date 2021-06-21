from django.contrib import admin
from django.contrib.auth import models

from .models import Profile

# Register your models here.

admin.site.register(Profile)
