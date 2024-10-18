from django.db import models
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)
    # name that has limit of 255 characters

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # create relationship between movies and genre
    # on_delete will provide cascading, when genre is deleted, all movies from that genre will be deleted too
    date_created = models.DateTimeField(default=timezone.now)
