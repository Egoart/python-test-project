from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from refshelf import models as refmodels
from books import models as bookmodels

#Edit Authors

class AuthorCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView ):
    model = refmodels.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.Authors
    success_url = reverse_lazy('refshelf:authors')

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

#Edit Genre

class GenreCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class GenreUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class GenreDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.Genre
    success_url = reverse_lazy('refshelf:genres')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Publisher

class PublisherCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherDelete(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = refmodels.Publisher
    success_url = reverse_lazy('refshelf:publishers')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Series

class SeriesCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = refmodels.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = refmodels.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = refmodels.BookSeries
    success_url = reverse_lazy('refshelf:serieses')

    def test_func(self):
        return self.request.user.profile.sale_staff == True


def resource_create(request):
    return render(request, 'stmanager/create_res.html')

class BookCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = bookmodels.Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = bookmodels.Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class BookDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = bookmodels.Book
    success_url = reverse_lazy('books:books')

    def test_func(self):
        return self.request.user.profile.sale_staff == True
