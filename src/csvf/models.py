from django.db import models

# Create your models here.

class CsvImport(models.Model):
    file_import = models.FileField(
        verbose_name='CSV файл',
        upload_to='csv-data'
    )
    file_uploaded = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )

    def __str__(self) -> str:
        return f'ID: {self.id}'

    class Meta:
        verbose_name = 'Файл импорта книг'
        verbose_name_plural = 'Файлы импорта книг'