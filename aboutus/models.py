from django.db import models

# Create your models here.
class Movie(models.Model):
    # poster image
    name = models.CharField(max_length=256)
    duration = models.IntegerField(default=0)
    grade = models.CharField(max_length=256)
    poster = models.CharField(max_length=256, default='')


    def __str__(self):
        return self.name
