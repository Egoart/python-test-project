from django.db import models
from django.urls import reverse


class Authors(models.Model):
    first_name = models.CharField(
        verbose_name='Имя автора', 
        max_length=20
        )
    last_name = models.CharField(
        verbose_name='Фамилия автора', 
        max_length=20
        )

    def __str__(self) -> str:
        return f' {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('refshelf:author', kwargs={'pk': self.pk})    

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Genre(models.Model):
    genre_name = models.CharField(
        verbose_name='Название жанра',
        max_length=20
    )
    genre_description = models.TextField(
        verbose_name='Описание жанра',
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return f'{self.genre_name}'

    def get_absolute_url(self):
        return reverse('refshelf:genre', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Publisher(models.Model):
    publisher_name = models.CharField(
        verbose_name='Издательство',
        max_length=20
    )
    publisher_description = models.TextField(
        verbose_name='Информация об издательстве',
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return f'Издательство {self.publisher_name}'

    def get_absolute_url(self):
        return reverse('refshelf:publisher', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

class BookSeries(models.Model):
    series_name = models.CharField(
        verbose_name='Серия',
        max_length=100
    )
    series_description = models.TextField(
        verbose_name='Описание серии',
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return f'Серия {self.series_name}'

    def get_absolute_url(self):
        return reverse('refshelf:series', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'