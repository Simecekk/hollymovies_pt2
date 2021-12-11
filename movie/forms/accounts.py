from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from movie.models import UserProfile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        UserProfile.objects.create(user=user)
        return user
