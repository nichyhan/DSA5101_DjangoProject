from django.contrib import admin

# Register your models here.
from .models import Movie
from .models import Genre
admin.site.register(Movie)
admin.site.register(Genre)