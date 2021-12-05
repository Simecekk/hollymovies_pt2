from django import forms
from django.core.exceptions import ValidationError


class UsernameNotDavidField(forms.CharField):
    def validate(self, value):
        if value == 'David':
            raise ValidationError('Username cannot be David')
