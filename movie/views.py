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
