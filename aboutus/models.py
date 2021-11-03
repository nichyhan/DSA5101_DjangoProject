from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=256, default='')
    duration = models.IntegerField(default=0)
    poster = models.CharField(max_length=256, default='')
    released = models.DateField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

