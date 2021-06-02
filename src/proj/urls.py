"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from airports import views as airports_views
from refshelf import views as refshelf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/<int:pk>/', refshelf_views.AuthorDetails.as_view(), name='author'),
    path('authors/', refshelf_views.AuthorList.as_view(), name='authors'),
    path('author_create/', refshelf_views.AuthorCreate.as_view(), name='author_create'),
    path('author_update/<int:pk>/', refshelf_views.AuthorUpdate.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', refshelf_views.AuthorDelete.as_view(), name='author_delete'),
    path('genre/<int:pk>/', refshelf_views.GenreDetails.as_view(), name='genre'),
    path('genres/', refshelf_views.GenreList.as_view(), name='genres'),
    path('genre_create/', refshelf_views.GenreCreate.as_view(), name='genre_create'),
    path('genre_update/<int:pk>/', refshelf_views.GenreUpdate.as_view(), name='genre_update'),
    path('genre_delete/<int:pk>/', refshelf_views.GenreDelete.as_view(), name='genre_delete'),
    path('publisher/<int:pk>/', refshelf_views.PublisherDetails.as_view(), name='publisher'),
    path('publishers/', refshelf_views.PublisherList.as_view(), name='publishers'),
    path('publisher_create/', refshelf_views.PublisherCreate.as_view(), name='publisher_create'),
    path('publisher_update/<int:pk>/', refshelf_views.PublisherUpdate.as_view(), name='publisher_update'),
    path('publisher_delete/<int:pk>/', refshelf_views.PublisherDelete.as_view(), name='publisher_delete'),
    path('series/<int:pk>/', refshelf_views.SeriesDetails.as_view(), name='series'),
    path('serieses/', refshelf_views.SeriesList.as_view(), name='serieses'),
    path('series_create/', refshelf_views.SeriesCreate.as_view(), name='series_create'),
    path('series_update/<int:pk>/', refshelf_views.SeriesUpdate.as_view(), name='series_update'),
    path('series_delete/<int:pk>/', refshelf_views.SeriesDelete.as_view(), name='series_delete'),
    path('<code>', airports_views.airports),
    path('', airports_views.airports_home)
]
