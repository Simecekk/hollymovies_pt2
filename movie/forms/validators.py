from django.core.exceptions import ValidationError


def validate_username_is_not_david(value):
    if value == 'David':
        raise ValidationError('Username cannot be David')


def validate_capitalized(value):
    if value[0].islower():
        raise ValidationError('First letter must be uppercase')
