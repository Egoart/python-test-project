from django.shortcuts import render

from . import models 

# Create your views here.

def author(request, author_id):
    author = models.Authors.objects.get(pk=author_id)
    ctx = {
        'author': author
    }
    return render(request, template_name='author.html', context=ctx)


def author_list(request):
    author_list = models.Authors.objects.all()
    ctx = {
        'author_list': author_list
    }
    return render(request, template_name='author_list.html', context=ctx)

def genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre': genre
    }
    return render(request, template_name='genre.html', context=ctx)


def genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'genre_list': genre_list
    }
    return render(request, template_name='genre_list.html', context=ctx)

def publisher(request, publisher_id):
    publisher = models.Publisher.objects.get(pk=publisher_id)
    ctx = {
        'publisher': publisher
    }
    return render(request, template_name='publisher.html', context=ctx)


def publisher_list(request):
    publisher_list = models.Publisher.objects.all()
    ctx = {
        'publisher_list': publisher_list
    }
    return render(request, template_name='publisher_list.html', context=ctx)

def series(request, series_id):
    series = models.BookSeries.objects.get(pk=series_id)
    ctx = {
        'series': series
    }
    return render(request, template_name='series.html', context=ctx)


def series_list(request):
    series_list = models.BookSeries.objects.all()
    ctx = {
        'series_list': series_list
    }
    return render(request, template_name='series_list.html', context=ctx)