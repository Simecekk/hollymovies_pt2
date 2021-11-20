from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from movie.models import Movie, Genre


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'generic/homepage.html', context=context)


def movie_list_view(request):
    context = {
        'movies': Movie.objects.all().order_by('-likes', '-rating'),
    }
    return TemplateResponse(request, 'movies/list.html', context=context)


def movie_detail_view(request, pk):
    context = {
        'movie': get_object_or_404(Movie, pk=pk)
    }
    return TemplateResponse(request, 'movies/detail.html', context=context)


def genre_detail_view(request, pk):
    context = {
        'genre': get_object_or_404(Genre, pk=pk)
    }
    return TemplateResponse(request, 'genres/detail.html', context=context)


def testing_cheatsheet_view(request):
    # python list[0]
    # template language jinja2 list.0

    # python dict['key']
    # template language jinja2 dict.key
    context = {
        'list': ['index0', 'index1'],
        'dict': {
            'key': 'value',
            'key2': 'value2'
        }
    }
    return TemplateResponse(request, 'generic/data_types_testing.html', context=context)
