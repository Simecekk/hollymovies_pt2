from django.urls import path
from movie.views import homepage_view, movie_list_view, movie_detail_view, genre_detail_view, testing_cheatsheet_view, \
    genre_list_view, actor_list_view, director_list_view, actor_detail_view, director_detail_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movie/list/', movie_list_view, name='movie-list'),
    path('movie/<int:pk>/', movie_detail_view, name='movie-detail'),
    path('genre/<int:pk>/', genre_detail_view, name='genre-detail'),
    path('genre/list/', genre_list_view, name='genre-list'),
    path('actor/list/', actor_list_view, name='actor-list'),
    path('director/list/', director_list_view, name='director-list'),
    path('actor/<int:pk>/', actor_detail_view, name='actor-detail'),
    path('director/<int:pk>/', director_detail_view, name='director-detail'),
    path('testing_data_types_in_templates/', testing_cheatsheet_view, name='data_types_testing'),
]
