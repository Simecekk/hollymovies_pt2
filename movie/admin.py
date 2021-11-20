from django.contrib import admin
from movie.models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'likes', 'rating', 'created']


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
