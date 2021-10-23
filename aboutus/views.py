from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    return HttpResponse("About us")

def movie(request):
    m = Movie.objects.all()
    return render(request, 'movie.html', { 'movies': m })