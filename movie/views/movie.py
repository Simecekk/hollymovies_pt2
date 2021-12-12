from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView

from movie.views.mixins import DeleteSuccessMixin
from movie.forms import MovieForm, ActorForm, GenreForm
from movie.models import Movie, Genre, MovieLikeRegister, Director, Actor


######################
# Class based views #
######################

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genres/detail.html'


class GenreListView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        context = {
            'genres': Genre.objects.all()
        }
        return TemplateResponse(request, 'genres/list.html', context=context)


class GenreCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    template_name = 'genres/create.html'
    form_class = GenreForm
    success_message = 'Successfully created genre %(name)s'
    permission_required = 'movie.add_genre'

    def get_success_url(self):
        return reverse('genre:detail', args=[self.object.id])


class GenreUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'genres/update.html'
    form_class = GenreForm
    model = Genre
    success_message = 'Successfully updated genre %(name)s'
    permission_required = 'movie.update_genre'

    def get_success_url(self):
        return reverse('genre:detail', args=[self.object.id])


class GenreDeleteView(DeleteSuccessMixin, PermissionRequiredMixin, DeleteView):
    model = Genre
    permission_required = 'movie.delete_genre'

    def get_success_message(self):
        return f'Successfully deleted genre name: {self.object.name}'

    def get_success_url(self):
        return reverse('genre:list')


class MovieListView(ListView):
    queryset = Movie.objects.all().order_by('-likes', '-rating')
    template_name = 'movies/list.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'

    @property
    def user_already_liked(self):
        if self.request.user.is_authenticated:
            user_liked_movie = MovieLikeRegister.objects.filter(user=self.request.user, movie=self.object).exists()
        else:
            user_liked_movie = False
        return user_liked_movie

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context.update({
            'already_liked': self.user_already_liked,
        })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.user_already_liked:
            return self.get(request, *args, **kwargs)
        self.object.likes += 1
        self.object.save(update_fields=['likes'])
        MovieLikeRegister.objects.create(
            user=request.user,
            movie=self.object,
        )
        return self.get(request, *args, **kwargs)


class MovieCreateView(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'movies/create.html'
    form_class = MovieForm
    success_message = 'Successfully created movie %(name)s'
    permission_required = 'movie.add_movie'

    def get_success_url(self):
        return reverse('movie:detail', args=[self.object.id])


class MovieUpdateView(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'movies/update.html'
    form_class = MovieForm
    model = Movie
    success_message = 'Successfully updated movie %(name)s'
    permission_required = 'movie.update_movie'

    def get_success_url(self):
        return reverse('movie:detail', args=[self.object.id])


class MovieDeleteView(DeleteSuccessMixin, PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Movie
    permission_required = 'movie.delete_movie'

    def get_success_message(self):
        return f'Successfully deleted movie name: {self.object.name}'

    def get_success_url(self):
        return reverse('movie:list')


class MovieDislikeView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        movie = get_object_or_404(Movie, pk=pk)
        movie.dislikes += 1
        movie.save(update_fields=['dislikes'])
        return redirect('movie:detail', pk=pk)


class ActorListView(TemplateView):
    template_name = 'actors/list.html'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actors/detail.html'


class ActorCreateView(SuccessMessageMixin, CreateView):
    template_name = 'actors/create.html'
    form_class = ActorForm
    success_message = 'Successfully created actor %(first_name)s %(last_name)s'

    def get_success_url(self):
        return reverse('actor:detail', args=[self.object.id])


class ActorUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'actors/update.html'
    form_class = ActorForm
    model = Actor
    success_message = 'Successfully updated actor %(first_name)s %(last_name)s'

    def get_success_url(self):
        return reverse('actor:detail', args=[self.object.id])


class ActorDeleteView(DeleteSuccessMixin, DeleteView):
    model = Actor

    def get_success_message(self):
        return f'Successfully deleted actor name: {self.object.full_name}'

    def get_success_url(self):
        return reverse('actor:list')


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/detail.html'


########################
# Function based views #
########################

def genre_detail_view(request, pk):
    context = {
        'genre': get_object_or_404(Genre, pk=pk)
    }
    return TemplateResponse(request, 'genres/detail.html', context=context)


def genre_list_view(request):
    context = {
        'genres': Genre.objects.all(),
    }
    return TemplateResponse(request, 'genres/list.html', context=context)


def actor_list_view(request):
    return TemplateResponse(request, 'actors/list.html')


def actor_detail_view(request, pk):
    context = {
        'actor': get_object_or_404(Actor, pk=pk)
    }
    return TemplateResponse(request, 'actors/detail.html', context=context)


def movie_list_view(request):
    context = {
        'movies': Movie.objects.all().order_by('-likes', '-rating'),
    }
    return TemplateResponse(request, 'movies/list.html', context=context)


def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.user.is_authenticated:
        user_liked_movie = MovieLikeRegister.objects.filter(user=request.user, movie=movie).exists()
    else:
        user_liked_movie = False

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


def dislike_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.dislikes += 1
    movie.save(update_fields=['dislikes'])
    return redirect('movie:detail', pk=pk)


def director_list_view(request):
    return TemplateResponse(request, 'directors/list.html')


def director_detail_view(request, pk):
    context = {
        'director': get_object_or_404(Director, pk=pk)
    }
    return TemplateResponse(request, 'directors/detail.html', context=context)
