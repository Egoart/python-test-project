from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )  
    phone = models.CharField(
        max_length=12,
        verbose_name='Номер телефона'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город'
    )
    post_index = models.IntegerField(
        verbose_name='Индекс',
        default='220000'
    )
    address1 = models.CharField(
        max_length=200,
        verbose_name='Адрес 1'
    )
    address2 = models.CharField(
        max_length=200,
        verbose_name='Адрес 2'
    )
    user_details = models.TextField(
        max_length=1000,
        verbose_name='Дополнительно',
        blank=True,
        null=True
    )
    sale_staff = models.BooleanField(
        default=False,
        verbose_name='Сотрудник магазина'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            print('Profile created')