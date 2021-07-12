# Generated by Django 3.2.3 on 2021-07-06 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20210629_1652'),
        ('orders', '0002_alter_order_contact_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_ordered', to='carts.cart', verbose_name='Заказ'),
        ),
    ]
