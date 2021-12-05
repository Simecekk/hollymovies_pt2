from django import forms

from movie import choices
from movie.forms.validators import validate_capitalized, validate_username_is_not_david
from movie.forms.widgets import CustomDatetimeInput, BootstrapEmailInput
from movie.models import Movie, Actor, Genre


class DummyForm(forms.Form):
    int_field = forms.IntegerField(min_value=5, max_value=10, required=False)
    username = forms.CharField(
        required=False, empty_value='unknown',
        label='Dummy Username', validators=[validate_username_is_not_david]
    )
    email = forms.EmailField(required=False, widget=BootstrapEmailInput())
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput())
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=choices.DIFFICULTY_CHOICES, initial=choices.DIFFICULTY_CHOICE_HARD)

    def clean_username(self):
        return self.cleaned_data['username'].capitalize()

    def __init__(self, min_likes, *args, **kwargs):
        super(DummyForm, self).__init__(*args, **kwargs)
        queryset = Movie.objects.filter(likes__gte=min_likes)
        self.fields['movie'].queryset = queryset
        self.fields['movies'].queryset = queryset

# class MovieForm(forms.Form):
#     name = forms.CharField(max_length=512)
#     description = forms.CharField(widget=forms.Textarea)
#     likes = forms.IntegerField(initial=0)
#     dislikes = forms.IntegerField(initial=0)
#     rating = forms.FloatField(max_value=5, min_value=0, initial=0)
#     genre = forms.ModelChoiceField(required=False, queryset=Genre.objects.all())


class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=512, validators=[validate_capitalized])

    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genre']
        # fields = '__all__'


class ActorForm(forms.ModelForm):
    born_at = forms.DateTimeField(widget=CustomDatetimeInput)

    class Meta:
        model = Actor
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
