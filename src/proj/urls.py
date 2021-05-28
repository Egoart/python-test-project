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
    path('author/<int:author_id>/', refshelf_views.author, name='author'),
    path('authors/', refshelf_views.author_list, name='authors'),
    path('genre/<int:genre_id>/', refshelf_views.genre, name='genre'),
    path('genres/', refshelf_views.genre_list, name='genres'),
    path('publisher/<int:publisher_id>/', refshelf_views.publisher, name='publisher'),
    path('publishers/', refshelf_views.publisher_list, name='publishers'),
    path('series/<int:series_id>/', refshelf_views.series, name='series'),
    path('serieses/', refshelf_views.series_list, name='serieses'),
    path('<code>', airports_views.airports),
    path('', airports_views.airports_home)
]
