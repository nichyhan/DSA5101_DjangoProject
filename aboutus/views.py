from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Genre


def index(request):
    return render(request, 'aboutus.html')

def movie(request):
    m = Movie.objects.all()
    g = Genre.objects.all()
    return render(request, 'movie.html', { 'movies': m, 'genre': g})

def sortbyname(request):
    movies_by_name = Movie.objects.order_by('name')[:]
    g = Genre.objects.all()
    return render(request, 'movie.html', {'movies': movies_by_name, 'genre': g})

def durationascending(request):
    movies_by_duration = Movie.objects.order_by('duration')[:]
    g = Genre.objects.all()
    return render(request, 'movie.html', {'movies': movies_by_duration, 'genre': g})

def durationdecending(request):
    movies_by_duration = Movie.objects.order_by('-duration')[:]
    g = Genre.objects.all()
    return render(request, 'movie.html', {'movies': movies_by_duration, 'genre': g})

def sortbyreleased(request):
    movies_by_released = Movie.objects.order_by('released')[:]
    g = Genre.objects.all()
    return render(request, 'movie.html', {'movies': movies_by_released, 'genre': g})

def filter(request):
    g = Genre.objects.all()
    selected_genre = request.POST.getlist('genre_checkbox')
    selected_sort = request.POST.getlist('sort_dropdown')

    movies = Movie.objects.all()

    return render(request, 'movie.html', {'movies': movies, 'genre': g, 'selected_genre': selected_genre, 'selected_sort':selected_sort})


