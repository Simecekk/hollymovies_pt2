from django.urls import path

from movie.views import homepage_view, MovieListView, MovieDetailView, GenreDetailView, TestingCheatSheetView, \
    GenreListView, ActorListView, director_list_view, ActorDetailView, DirectorDetailView, DislikeMovieView, \
    CinemaListView, CinemaDetailView, ScreeningDetailView, DummyFormView, CreateMovieView, CreateActorView, \
    UpdateMovieView

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movie/list/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/list/', GenreListView.as_view(), name='genre-list'),
    path('actor/list/', ActorListView.as_view(), name='actor-list'),
    path('director/list/', director_list_view, name='director-list'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('dislike_movie/<int:pk>/', DislikeMovieView.as_view(), name='dislike-movie'),
    path('testing_data_types_in_templates/', TestingCheatSheetView.as_view(), name='data_types_testing'),
    path('cinema/list/', CinemaListView.as_view(), name='cinema-list'),
    path('cinema/<int:pk>/', CinemaDetailView.as_view(), name='cinema-detail'),
    path('screening/<int:pk>/', ScreeningDetailView.as_view(), name='screening-detail'),
    path('dummy_forms/', DummyFormView.as_view(), name='dummy_form'),
    path('create/movie/', CreateMovieView.as_view(), name='create_movie'),
    path('create/actor/', CreateActorView.as_view(), name='create_actor'),
    path('update/movie/<int:pk>/', UpdateMovieView.as_view(), name='update_movie'),
]
