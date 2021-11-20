from django.urls import path
from movie.views import homepage_view, movie_list_view, movie_detail_view


urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movie/list/', movie_list_view, name='movie-list'),
    path('movie/<int:pk>/', movie_detail_view, name='movie-detail'),
]
