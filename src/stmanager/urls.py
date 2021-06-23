from django.urls import path

from stmanager import views as manager_views

app_name = 'stmanager'

urlpatterns = [
    path('series_create/', manager_views.SeriesCreate.as_view(), name='series_create'),
    path('series_update/<int:pk>/', manager_views.SeriesUpdate.as_view(), name='series_update'),
    path('series_delete/<int:pk>/', manager_views.SeriesDelete.as_view(), name='series_delete'),
    path('create_res/', manager_views.resource_create, name='create_res'),
    path('publisher_create/', manager_views.PublisherCreate.as_view(), name='publisher_create'),
    path('publisher_update/<int:pk>/', manager_views.PublisherUpdate.as_view(), name='publisher_update'),
    path('publisher_delete/<int:pk>/', manager_views.PublisherDelete.as_view(), name='publisher_delete'),
    path('genre_create/', manager_views.GenreCreate.as_view(), name='genre_create'),
    path('genre_update/<int:pk>/', manager_views.GenreUpdate.as_view(), name='genre_update'),
    path('genre_delete/<int:pk>/', manager_views.GenreDelete.as_view(), name='genre_delete'),
    path('author_create/', manager_views.AuthorCreate.as_view(), name='author_create'),
    path('author_update/<int:pk>/', manager_views.AuthorUpdate.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', manager_views.AuthorDelete.as_view(), name='author_delete'),
]
