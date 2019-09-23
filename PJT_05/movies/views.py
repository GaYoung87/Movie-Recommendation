from django.shortcuts import render
from .models import Movie
# from datetime import datetime

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def new(request):
    return render(request, 'movies/new.html')


def create(request):
    return render(request, 'movies/create.html')


