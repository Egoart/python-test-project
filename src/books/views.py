from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from . import models
from carts.models import CartItems
from django.db.models import Q
from django.db.models import Sum, Count
import random

# Create your views here.


class BookDetails(DetailView):
    model = models.Book


    def get_context_data(self, **kwargs):
        context = super(BookDetails, self).get_context_data(**kwargs)
        genres = self.get_object().book_genres.all()
        if genres.count() == 1:
            genres1 = self.get_object().book_genres.all()[0]
            filtered_book = models.Book.objects.filter(
            Q(book_genres=genres1)
            ).exclude(pk=self.get_object().pk)
        else:
            genres1 = self.get_object().book_genres.all()[0]
            genres2 = self.get_object().book_genres.all()[1]
            filtered_book = models.Book.objects.filter(
            Q(book_genres=genres1) | Q(book_genres=genres2)
            ).exclude(pk=self.get_object().pk)
        
        if filtered_book.count() >= 3:    
            rand_filt_book = random.sample(list(filtered_book), 3)
            context['related_items'] = rand_filt_book
        else: 
            context['related_items'] = filtered_book
        return context

class BookList(ListView):
    model = models.Book

    def get_queryset(self):
        qs = super().get_queryset()
        bsearch = self.request.GET.get('bsearch')
        if bsearch:
            return qs.filter(Q(book_title__icontains=bsearch) | Q(book_authors__last_name__icontains=bsearch) | Q(book_authors__first_name__icontains=bsearch)) 
        return qs

class HomeView(TemplateView):
    template_name='books/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = models.Book.objects.all().order_by('-id')[:3]
        context['recommended_books'] = models.Book.objects.all().filter(is_recommended=True)
        context['total_books'] = models.Book.objects.aggregate(tot = Count('book_title'))
        context['sold_books'] = models.Book.objects.annotate(tot = Sum('cartitems__quantity')).order_by('-tot')[:3]

        return context

