from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from books.models import Book



# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='carts',
        verbose_name='Корзина',
        on_delete=models.PROTECT
    )
    cart_created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False,
        auto_now_add=True
    )
    cart_modified = models.DateTimeField(
        verbose_name='Модифицировано',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return f'Корзина # {self.pk}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @property
    def cart_total_price(self):
        cart_total_price = 0
        items_incart = self.cart_items.all()
        for item in items_incart:
            cart_total_price += item.item_total_price
        return cart_total_price

    @property
    def book_count(self):
        total_sold = 0
        items_incart = self.cart_items.all()
        if self.cart_items.book:
            for item in items_incart:
                total_sold += item.quantity
        return total_sold


class CartItems(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_items',

    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )
    quantity = models.IntegerField(
        verbose_name='Количество',
        default=1
    )
    item_price = models.DecimalField(
        verbose_name='Стоимость книги, BYN', 
        max_digits=5,
        decimal_places = 2
    )
    ct_item_created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False,
        auto_now_add=True
    )
    ct_item_modified = models.DateTimeField(
        verbose_name='Модифицировано',
        auto_now=True,
        auto_now_add=False
    )
    class Meta:
        verbose_name = 'Товары в козине'
        verbose_name_plural = 'Товары в корзине'

    @property
    def item_total_price(self):
        return self.item_price*self.quantity

    
