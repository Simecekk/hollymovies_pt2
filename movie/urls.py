from django.urls import path
from movie.views import homepage_view, MovieListView, MovieDetailView, genre_detail_view, testing_cheatsheet_view, \
    GenreListView, ActorListView, director_list_view, actor_detail_view, director_detail_view, dislike_movie_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movie/list/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('genre/<int:pk>/', genre_detail_view, name='genre-detail'),
    path('genre/list/', GenreListView.as_view(), name='genre-list'),
    path('actor/list/', ActorListView.as_view(), name='actor-list'),
    path('director/list/', director_list_view, name='director-list'),
    path('actor/<int:pk>/', actor_detail_view, name='actor-detail'),
    path('director/<int:pk>/', director_detail_view, name='director-detail'),
    path('dislike_movie/<int:pk>/', dislike_movie_view, name='dislike-movie'),
    path('testing_data_types_in_templates/', testing_cheatsheet_view, name='data_types_testing'),
]
