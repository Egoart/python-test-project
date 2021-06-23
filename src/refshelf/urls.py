from django.urls import path

from refshelf import views as refshelf_views

app_name = 'refshelf'

urlpatterns = [
    path('author/<int:pk>/', refshelf_views.AuthorDetails.as_view(), name='author'),
    path('authors/', refshelf_views.AuthorList.as_view(), name='authors'),
    path('genre/<int:pk>/', refshelf_views.GenreDetails.as_view(), name='genre'),
    path('genres/', refshelf_views.GenreList.as_view(), name='genres'),
    path('publisher/<int:pk>/', refshelf_views.PublisherDetails.as_view(), name='publisher'),
    path('publishers/', refshelf_views.PublisherList.as_view(), name='publishers'),
    path('series/<int:pk>/', refshelf_views.SeriesDetails.as_view(), name='series'),
    path('serieses/', refshelf_views.SeriesList.as_view(), name='serieses'),
]
