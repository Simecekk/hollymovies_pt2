from django.contrib import admin
from django.utils import timezone
from datetime import timedelta

from movie.models import Movie, Genre, Actor, Director, Cinema, CinemaMovieScreening


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'likes', 'rating', 'created']


class GenreAdmin(admin.ModelAdmin):
    pass


class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', ]


class CinemaMovieScreeningAdmin(admin.ModelAdmin):

    @staticmethod
    def closed(obj):
        return obj.is_closed

    @staticmethod
    def soldout(obj):
        return obj.soldout

    list_display = ['cinema', 'movie', 'screening_start_at', 'minutes_duration', 'soldout', 'closed']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(CinemaMovieScreening, CinemaMovieScreeningAdmin)
