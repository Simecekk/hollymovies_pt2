from django import template
from django.shortcuts import reverse
from movie.models import Actor, Director

register = template.Library()


@register.inclusion_tag('generic/person_table.html', takes_context=True)
def movie_actor_table(context):
    movie = context['movie']
    context.update({
        'people': movie.actors.all(),
        'table_head': 'Actors'
    })
    return context


@register.inclusion_tag('generic/person_table.html', takes_context=True)
def movie_director_table(context):
    movie = context['movie']
    context.update({
        'people': movie.directors.all(),
        'table_head': 'Directors'
    })
    return context


@register.inclusion_tag('generic/person_table.html')
def all_actor_table():
    return {'people': Actor.objects.all()}


@register.inclusion_tag('generic/person_table.html')
def all_director_table():
    return {'people': Director.objects.all()}


@register.simple_tag(takes_context=True)
def can_like_message(context):
    already_liked = context['already_liked']
    if already_liked:
        return 'You have already liked this movie'
    else:
        return 'You can like this movie'
