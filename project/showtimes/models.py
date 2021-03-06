from django.db import models
from movielist.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(to=Movie, through='Screening')

    def __str__(self):
        return self.name


class Screening(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='Movie'
    )
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, verbose_name='Cinema'
    )
    date = models.DateTimeField(verbose_name='Screening time')
