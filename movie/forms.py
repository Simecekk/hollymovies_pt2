from django import forms

from movie.models import Movie


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


DIFFICULTY_CHOICES = (
    (1, 'Easy'),
    (2, 'medium'),
    (3, 'hard'),
    (4, 'insane'),
)


class DummyForm(forms.Form):
    int_field = forms.IntegerField(min_value=5, max_value=10, required=False)
    username = forms.CharField(required=False, empty_value='unknown', label='Dummy Username')
    email = forms.EmailField(required=False)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput)
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
