from django.db import models


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
        return f'Автор {self.first_name} {self.last_name}'

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
        return f'Название жанра {self.genre_name}'

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

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'