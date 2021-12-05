from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from movie.forms import DummyForm
from movie.models import Movie, Genre, Actor, Director


######################
# Class based views #
######################

class TestingCheatSheetView(TemplateView):
    template_name = 'generic/data_types_testing.html'

    # python list[0]
    # template language jinja2 list.0

    # python dict['key']
    # template language jinja2 dict.key
    extra_context = {
        'list': ['index0', 'index1'],
        'dict': {
            'key': 'value',
            'key2': 'value2'
        }
    }


class DummyFormView(FormView):
    template_name = 'generic/dummy_forms.html'
    success_url = reverse_lazy('dummy_form')
    initial = {'username': 'Honza'}

    def get_form(self, form_class=None):
        return DummyForm(10, **self.get_form_kwargs())

    def form_valid(self, form):
        int_field = form.cleaned_data['int_field']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        datetime_test = form.cleaned_data['datetime_test']
        movie = form.cleaned_data['movie']
        movies = form.cleaned_data['movies']
        difficulty = form.cleaned_data['difficulty']

        print(int_field)
        print(username)
        print(email)
        print(datetime_test)
        print(difficulty)
        print(movie)
        print(movies)

        return super(DummyFormView, self).form_valid(form)

    def form_invalid(self, form):
        print('Form was invalid!!!')
        return super(DummyFormView, self).form_invalid(form)


# class DummyFormView(View):
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': DummyForm()
#         }
#         return TemplateResponse(request, 'dummy_forms.html', context=context)
#
#     def post(self, request, *args, **kwargs):
#         bounded_form = DummyForm(data=request.POST)
#
#         if not bounded_form.is_valid():
#             context = {'form': bounded_form}
#             return TemplateResponse(request, 'dummy_forms.html', context=context)
#
#         # NOTE Když pracujeme s daty ve formě, vždy použíjme cleaned_date
#         int_field = bounded_form.cleaned_data['int_field']
#         username = bounded_form.cleaned_data['username']
#         email = bounded_form.cleaned_data['email']
#         datetime_test = bounded_form.cleaned_data['datetime_test']
#         movie = bounded_form.cleaned_data['movie']
#         movies = bounded_form.cleaned_data['movies']
#         difficulty = bounded_form.cleaned_data['difficulty']
#
#         print(int_field)
#         print(username)
#         print(email)
#         print(datetime_test)
#         print(difficulty)
#         print(movie)
#         print(movies)
#
#         return self.get(request, *args, **kwargs)


########################
# Function based views #
########################

def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
        'number_of_directors': Director.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'generic/homepage.html', context=context)


def testing_cheatsheet_view(request):
    # python list[0]
    # template language jinja2 list.0

    # python dict['key']
    # template language jinja2 dict.key
    context = {
        'list': ['index0', 'index1'],
        'dict': {
            'key': 'value',
            'key2': 'value2'
        }
    }
    return TemplateResponse(request, 'generic/data_types_testing.html', context=context)