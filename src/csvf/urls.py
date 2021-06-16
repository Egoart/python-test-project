from django.urls import path
from .views import csv_import_view

app_name = 'csvf'

urlpatterns = [
    path('csv_import', csv_import_view, name='csv_import'),
]