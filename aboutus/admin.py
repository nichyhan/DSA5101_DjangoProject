from django.contrib import admin

# Register your models here.
from .models import Movie
from .models import Genre
from .models import Grade
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Grade)