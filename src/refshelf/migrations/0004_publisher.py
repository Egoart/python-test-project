# Generated by Django 3.2.3 on 2021-05-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refshelf', '0003_auto_20210523_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=20, verbose_name='Издательство')),
                ('publisher_description', models.TextField(blank=True, null=True, verbose_name='Информация об издательстве')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
    ]