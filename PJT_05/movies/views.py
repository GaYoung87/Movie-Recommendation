from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

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
    # 이전 페이지로부터 전송받은 데이터를 데이터 베이스에 저장한다.
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    # 원래 open_date가 맞는데, model 생성시 open_data라고 했음..ㅠ
    open_data = request.GET.get('open_data')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_data=open_data,
    genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()
    
    return render(request, 'movies/create.html')


def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    open_data = movie.open_data
    open_data = open_data.strftime("%Y-%m-%d")
    context = {
        'movie': movie,
        'open_data': open_data,
    }

    return render(request, 'movies/edit.html', context)


def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_data = request.GET.get('open_data')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')

    movie.save()

    return render(request, 'movies/update.html')


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return render(request, 'movies/delete.html')