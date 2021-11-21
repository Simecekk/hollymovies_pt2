from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect

from movie.models import Movie, Genre, MovieLikeRegister, Actor, Director


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
        'number_of_directors': Director.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'generic/homepage.html', context=context)


def movie_list_view(request):
    context = {
        'movies': Movie.objects.all().order_by('-likes', '-rating'),
    }
    return TemplateResponse(request, 'movies/list.html', context=context)


def genre_list_view(request):
    context = {
        'genres': Genre.objects.all(),
    }
    return TemplateResponse(request, 'genres/list.html', context=context)


def actor_list_view(request):
    return TemplateResponse(request, 'actors/list.html')


def director_list_view(request):
    return TemplateResponse(request, 'directors/list.html')


def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    user_liked_movie = MovieLikeRegister.objects.filter(user=request.user, movie=movie).exists()
    if request.method == 'POST' and request.user.is_authenticated and not user_liked_movie:
        movie.likes += 1
        movie.save(update_fields=['likes'])
        MovieLikeRegister.objects.create(
            user=request.user,
            movie=movie,
        )
        user_liked_movie = True

    context = {
        'movie': movie,
        'already_liked': user_liked_movie
    }
    return TemplateResponse(request, 'movies/detail.html', context=context)


def genre_detail_view(request, pk):
    context = {
        'genre': get_object_or_404(Genre, pk=pk)
    }
    return TemplateResponse(request, 'genres/detail.html', context=context)


def director_detail_view(request, pk):
    context = {
        'director': get_object_or_404(Director, pk=pk)
    }
    return TemplateResponse(request, 'directors/detail.html', context=context)


def actor_detail_view(request, pk):
    context = {
        'actor': get_object_or_404(Actor, pk=pk)
    }
    return TemplateResponse(request, 'actors/detail.html', context=context)


def dislike_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.dislikes += 1
    movie.save(update_fields=['dislikes'])
    return redirect('movie-detail', pk=pk)


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
