from django.contrib import admin
from movie.models import Movie, Genre, Actor, Director


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'likes', 'rating', 'created']


class GenreAdmin(admin.ModelAdmin):
    pass


class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
