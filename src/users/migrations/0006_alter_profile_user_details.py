# Generated by Django 3.2.3 on 2021-06-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_details_profile_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_details',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Дополнительно'),
        ),
    ]
