from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from . import models

# Create your views here.


class BookDetails(DetailView):
    model = models.Book

class BookList(ListView):
    model = models.Book

class HomeView(TemplateView):
    template_name='books/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = models.Book.objects.all().order_by('-id')[:4]
        context['recommended_books'] = models.Book.objects.all().filter(is_recommended=True)
        return context