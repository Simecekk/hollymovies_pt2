from django import template

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


@register.simple_tag(takes_context=True)
def can_like_message(context):
    already_liked = context['already_liked']
    if already_liked:
        return 'You have already liked this movie'
    else:
        return 'You can like this movie'
