from django.urls import path
from movie.views import homepage_view, movie_list_view, movie_detail_view, genre_detail_view, testing_cheatsheet_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movie/list/', movie_list_view, name='movie-list'),
    path('movie/<int:pk>/', movie_detail_view, name='movie-detail'),
    path('genre/<int:pk>/', genre_detail_view, name='genre-detail'),
    path('testing_data_types_in_templates/', testing_cheatsheet_view, name='data_types_testing'),
]
