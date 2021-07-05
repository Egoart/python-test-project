from django.urls import path

from books import views as book_views

app_name = 'books'

urlpatterns = [
    path('book/<int:pk>/', book_views.BookDetails.as_view(), name='book'),
    path('books/', book_views.BookList.as_view(), name='books'),
    #path('book_update/<int:pk>/', refshelf_views.AuthorUpdate.as_view(), name='author_update'),
    #path('book_delete/<int:pk>/', refshelf_views.AuthorDelete.as_view(), name='author_delete')
]
