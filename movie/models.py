from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return f'{self.name} : {self.id}'


class Movie(BaseModel):
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True, default='')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ], default=0)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movies')

    def __str__(self):
        return f'{self.name} : {self.id}'


class Person(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()
    born_at = models.DateTimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.pk}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Actor(Person):
    movies = models.ManyToManyField(Movie, related_name='actors')

    def get_detail_url(self):
        return reverse('actor-detail', args=[self.pk])


class Director(Person):
    movies = models.ManyToManyField(Movie, related_name='directors')

    def get_detail_url(self):
        return reverse('director-detail', args=[self.pk])


class MovieLikeRegister(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Cinema(BaseModel):
    name = models.CharField(max_length=512)
    location = models.CharField(max_length=512)

    class Meta:
        unique_together = ('name', 'location')

    def __str__(self):
        return f'{self.name} : {self.location}'


class CinemaMovieScreening(BaseModel):
    screening_start_at = models.DateTimeField()
    minutes_duration = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='screenings')
    number_of_tickets = models.IntegerField()
    ticket_price = models.FloatField()
    sold_tickets = models.IntegerField(default=0)

    @property
    def available_tickets(self):
        return self.number_of_tickets - self.sold_tickets

    @property
    def soldout(self):
        return self.available_tickets <= 0

    @property
    def is_closed(self):
        now = timezone.now()
        is_active = now > (self.screening_start_at + timedelta(minutes=self.minutes_duration))
        return is_active
