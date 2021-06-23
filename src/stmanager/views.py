from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from refshelf import models

#Edit Authors

class AuthorCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView ):
    model = models.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Authors
    success_url = reverse_lazy('refshelf:authors')

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

#Edit Genre

class GenreCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class GenreUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class GenreDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Genre
    success_url = reverse_lazy('refshelf:genres')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Publisher

class PublisherCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Publisher
    fields = ['publisher_name', 'publisher_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class PublisherDelete(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('refshelf:publishers')

    def test_func(self):
        return self.request.user.profile.sale_staff == True

#Edit Series

class SeriesCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.BookSeries
    fields = ['series_name', 'series_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True

class SeriesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.BookSeries
    success_url = reverse_lazy('refshelf:serieses')

    def test_func(self):
        return self.request.user.profile.sale_staff == True


def resource_create(request):
    return render(request, 'stmanager/create_res.html')
