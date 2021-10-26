from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    return render(request, 'aboutus.html')

def movie(request):
    m = Movie.objects.all()
    return render(request, 'movie.html', { 'movies': m })
