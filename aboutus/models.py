from django.db import models

# Create your models here.
class Movie(models.Model):
    # poster image
    name = models.CharField(max_length=256, default='')
    duration = models.IntegerField(default=0)
    grade = models.CharField(max_length=256, default='')
    poster = models.CharField(max_length=256, default='')
    genre = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name