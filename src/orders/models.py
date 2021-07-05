from django.db import models
from django.db.models.fields.related import ForeignKey

from carts import models as cart_model

# Create your models here.

class Order(models.Model):

    class OrderStatus(models.Model):
        NEW = 'Новый'
        PRC= 'В обработке'
        FLD = 'Неудавшийся'
        CLS = 'Исполненный'

        ORDER_CHOICES = [
            (NEW, 'Новый'),
            (PRC, 'В обработке'),
            (FLD, 'Неудавшийся'),
            (CLS, 'Исполненный'),
        ]
    cart = ForeignKey(
        cart_model.Cart,
        on_delete=models.PROTECT,
        verbose_name='Заказ'
    )
    contact_info = models.CharField(
        verbose_name='Контактный номер',
        max_length=11,
    )
    order_status = models.CharField(
        verbose_name='Статус заказа',
        max_length=11,
        choices=OrderStatus.ORDER_CHOICES,
        default=OrderStatus.NEW
    )
    order_created = models.DateTimeField(
        verbose_name='Создан',
        auto_now=False,
        auto_now_add=True
    )
    order_modified = models.DateTimeField(
        verbose_name='Модифицирован',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:
        return f' Заказ ID: {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'