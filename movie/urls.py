from django.urls import path, include

from movie.views.cinema import CinemaListView, CinemaDetailView, ScreeningDetailView
from movie.views.generic import homepage_view, TestingCheatSheetView, DummyFormView
from movie.views.movie import MovieListView, MovieDetailView, MovieDeleteView, GenreDetailView, MovieCreateView, \
    MovieUpdateView, MovieDislikeView, GenreListView, ActorListView, ActorDetailView, ActorUpdateView, ActorCreateView, \
    ActorDeleteView, director_list_view, DirectorDetailView, GenreUpdateView, GenreCreateView, GenreDeleteView

movie_urlpatterns = ([
    path('list/', MovieListView.as_view(), name='list'),
    path('detail/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('dislike/<int:pk>/', MovieDislikeView.as_view(), name='dislike'),
    path('create/', MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete'),
], 'movie')

genre_urlpatterns = ([
    path('detail/<int:pk>/', GenreDetailView.as_view(), name='detail'),
    path('list/', GenreListView.as_view(), name='list'),
    path('update/<int:pk>/', GenreUpdateView.as_view(), name='update'),
    path('create/', GenreCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', GenreDeleteView.as_view(), name='delete')
], 'genre')

actor_urlpatterns = ([
    path('list/', ActorListView.as_view(), name='list'),
    path('detail/<int:pk>/', ActorDetailView.as_view(), name='detail'),
    path('create/', ActorCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
], 'actor')


director_urlpatterns = ([
    path('list/', director_list_view, name='list'),
    path('detail/<int:pk>/', DirectorDetailView.as_view(), name='detail'),
], 'director')


cinema_urlpatterns = ([
    path('list/', CinemaListView.as_view(), name='list'),
    path('detail/<int:pk>/', CinemaDetailView.as_view(), name='detail'),
], 'cinema')


screening_urlpatterns = ([
    path('detail/<int:pk>/', ScreeningDetailView.as_view(), name='detail'),
], 'screening')

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('testing_data_types_in_templates/', TestingCheatSheetView.as_view(), name='data_types_testing'),
    path('dummy_forms/', DummyFormView.as_view(), name='dummy_form'),
    path('movie/', include(movie_urlpatterns)),
    path('genre/', include(genre_urlpatterns)),
    path('actor/', include(actor_urlpatterns)),
    path('director/', include(director_urlpatterns)),
    path('cinema/', include(cinema_urlpatterns)),
    path('screening/', include(screening_urlpatterns))
]
