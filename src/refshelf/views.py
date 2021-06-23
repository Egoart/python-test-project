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

class GenreDetails(DetailView):
    model = models.Genre

class GenreList(ListView):
    model = models.Genre

class PublisherDetails(DetailView):
    model = models.Publisher

class PublisherList(ListView):
    model = models.Publisher

class SeriesDetails(DetailView):
    model = models.BookSeries

class SeriesList(ListView):
    model = models.BookSeries


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