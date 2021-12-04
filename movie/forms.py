from django import forms

from movie.models import Movie, Genre, Actor
from django.core.exceptions import ValidationError


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


DIFFICULTY_CHOICES = (
    (1, 'Easy'),
    (2, 'medium'),
    (3, 'hard'),
    (4, 'insane'),
)


def validate_username_is_not_david(value):
    if value == 'David':
        raise ValidationError('Username cannot be David')


class UsernameNotDavidField(forms.CharField):
    def validate(self, value):
        if value == 'David':
            raise ValidationError('Username cannot be David')


class DummyForm(forms.Form):
    int_field = forms.IntegerField(min_value=5, max_value=10, required=False)
    username = forms.CharField(required=False, empty_value='unknown', label='Dummy Username', validators=[validate_username_is_not_david])
    email = forms.EmailField(required=False)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput())
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)

    def clean_username(self):
        return self.cleaned_data['username'].capitalize()


# class MovieForm(forms.Form):
#     name = forms.CharField(max_length=512)
#     description = forms.CharField(widget=forms.Textarea)
#     likes = forms.IntegerField(initial=0)
#     dislikes = forms.IntegerField(initial=0)
#     rating = forms.FloatField(max_value=5, min_value=0, initial=0)
#     genre = forms.ModelChoiceField(required=False, queryset=Genre.objects.all())


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genre']
        # fields = ['__all__']


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name']
