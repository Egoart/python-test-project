from django.db import models
from django.urls import reverse
from refshelf import models as refbook



class Binding(models.Model):
    binding_type = models.CharField(
        verbose_name='Переплет',
        max_length=100
    )

    def __str__(self) -> str:
        return f' {self.binding_type}'   

    class Meta:
        verbose_name = 'Переплет'
        verbose_name_plural = 'Переплеты'


class Book(models.Model):
    
    class AgeRestr(models.Model):
        UNDERSIX = '0+'
        ABOVESIX = '6+'
        ABOVETWELVE = '12+'
        ABOVESIXTEEN ='16+'
        ABOVEEIGHTTEEN ='18+'

        AGE_CHOICES = [
            (UNDERSIX, '0+'),
            (ABOVESIX, '6+'),
            (ABOVETWELVE, '12+'),
            (ABOVESIXTEEN, '16+'),
            (ABOVEEIGHTTEEN, '18+')
        ]
    
    class BookFormat(models.Model):
        SUPERBIG = 'Сверхкрупный'
        BIG = 'Крупный'
        INTERM = 'Средний'
        SMALL ='Малый'
        SUPERSMALL ='Сверхмалый'

        FORMAT_CHOICES = [
            (SUPERBIG, 'Сверхкрупный'),
            (BIG, 'Крупный'),
            (INTERM, 'Средний'),
            (SMALL, 'Малый'),
            (SUPERSMALL, 'Сверхмалый')
        ]

    book_title = models.CharField(
        verbose_name='Название книги', 
        max_length=250
        )
    cover_picture = models.ImageField(
        verbose_name='Фото обложки',
        upload_to ='book//%Y/%m/%d/',
        blank=True, 
        null=True
    )
    book_price = models.DecimalField(
        verbose_name='Стоимость книги, BYN', 
        max_digits=5,
        decimal_places = 2
        )
    book_authors = models.ManyToManyField(
        refbook.Authors,
        verbose_name='Автор(ы)',
        related_name='books'
    )
    book_series = models.ForeignKey(
        refbook.BookSeries,
        on_delete=models.RESTRICT,
        verbose_name='Серия книг',
        related_name='books',
        blank=True, 
        null=True
    )
    book_genres = models.ManyToManyField(
        refbook.Genre,
        verbose_name='Жанр(ы)',
        related_name='books'
    )
    book_year = models.PositiveSmallIntegerField(
        verbose_name='Год издания'
    )
    book_pages = models.PositiveSmallIntegerField(
        verbose_name='Количество страниц'
    )
    book_icbn = models.CharField(
        verbose_name='Номер ISBN',
        max_length=200        
    )
    book_weight = models.PositiveSmallIntegerField(
        verbose_name='Вес книги'
    )
    book_publisher = models.ForeignKey(
        refbook.Publisher,
        on_delete=models.RESTRICT,
        verbose_name='Издательство',
        related_name='books'
    )
    book_format = models.CharField(
        verbose_name='Формат книги',
        max_length=25,
        choices=BookFormat.FORMAT_CHOICES,
        default=BookFormat.INTERM
    )
    book_bindings = models.ForeignKey(
        Binding,
        on_delete=models.RESTRICT,
        verbose_name='Переплет',
        related_name='books'
    )
    book_quantity = models.PositiveIntegerField(
        verbose_name='Количество книг на складе'
    )
    is_available = models.BooleanField(
        verbose_name='В наличии',
        default=True
    )
    is_recommended = models.BooleanField(
        verbose_name='Рекомендуемый товар',
        default=False,
        blank=True, 
        null=True
    )
    age_restrictions = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=3,
        choices=AgeRestr.AGE_CHOICES,
        default=AgeRestr.UNDERSIX
    )
    book_rating = models.IntegerField(
        verbose_name='Рейтинг',
        choices=((i,i) for i in range(11)) 
    )
    book_created = models.DateTimeField(
        verbose_name='Дата создания в каталоге',
        auto_now=False,
        auto_now_add=True
    )
    book_modified = models.DateTimeField(
        verbose_name='Дата последнего изменения',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:        
        return f' {self.book_title}'

    def get_absolute_url(self):
        return reverse('refshelf:author', kwargs={'pk': self.pk})    

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'









