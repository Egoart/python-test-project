from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . import models 

# Create your views here.

class AuthorDetails(DetailView):
    model = models.Authors

class AuthorList(ListView):
    model = models.Authors


class AuthorCreate(UserPassesTestMixin, CreateView ):
    model = models.Authors
    fields = ['first_name', 'last_name', 'picture']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = models.Authors
    fields = ['first_name', 'last_name', 'picture']

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = models.Authors
    success_url = reverse_lazy('refshelf:authors')

class GenreDetails(DetailView):
    model = models.Genre

class GenreList(ListView):
    model = models.Genre

class GenreCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Genre
    fields = ['genre_name', 'genre_description']

    def test_func(self):
        return self.request.user.profile.sale_staff == True 

class GenreUpdate(LoginRequiredMixin, UpdateView):
    model = models.Genre
    fields = ['genre_name', 'genre_description']

class GenreDelete(LoginRequiredMixin, DeleteView):
    model = models.Genre
    success_url = reverse_lazy('refshelf:genres')

class PublisherDetails(DetailView):
    model = models.Publisher

class PublisherList(ListView):
    model = models.Publisher

class PublisherCreate(LoginRequiredMixin, CreateView):
    model = models.Publisher
    fields = ['publisher_name', 'publisher_description']

class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = models.Publisher
    fields = ['publisher_name', 'publisher_description']

class PublisherDelete(LoginRequiredMixin, DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('refshelf:publishers')

class SeriesDetails(DetailView):
    model = models.BookSeries

class SeriesList(ListView):
    model = models.BookSeries

class SeriesCreate(LoginRequiredMixin, CreateView):
    model = models.BookSeries
    fields = ['series_name', 'series_description']

class SeriesUpdate(LoginRequiredMixin, UpdateView):
    model = models.BookSeries
    fields = ['series_name', 'series_description']

class SeriesDelete(LoginRequiredMixin, DeleteView):
    model = models.BookSeries
    success_url = reverse_lazy('refshelf:serieses')



# def series(request, series_id):
#     series = models.BookSeries.objects.get(pk=series_id)
#     ctx = {
#         'series': series
#     }
#     return render(request, template_name='series.html', context=ctx)


# def series_list(request):
#     series_list = models.BookSeries.objects.all()
#     ctx = {
#         'series_list': series_list
#     }
#     return render(request, template_name='series_list.html', context=ctx)