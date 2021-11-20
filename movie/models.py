from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    rating = models.FloatField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ], default=0)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movies')

    def __str__(self):
        return f'{self.name} : {self.id}'
