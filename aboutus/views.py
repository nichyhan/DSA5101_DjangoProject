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

# Already finished to sort from A-Z
def sortbyname(request):
    movies_by_name = Movie.objects.order_by('name')[:]
    g = Genre.objects.all()  # Do not edit 'g'. The values show in the checkbox.
    return render(request, 'movie.html', {'movies': movies_by_name, 'genre': g})

##### START EDIT HERE #####
# Add a function to sort by duration

# Add a function to sort by date released


def filter(request):
    g = Genre.objects.all() # Do not edit 'g'. The values show in the checkbox.
    selected_genre = request.POST.getlist('genre_checkbox') # Here are genre(s) that a user has selected.

    ##### START EDIT HERE #####
    # Edit the line below to filter by selected_genre
    movies = Movie.objects.all()

    return render(request, 'movie.html', {'movies': movies, 'genre': g,  'selected_genre': selected_genre})

