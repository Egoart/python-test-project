from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . import models

# Create your views here.


class BookDetails(DetailView):
    model = models.Book

class BookList(ListView):
    model = models.Book
