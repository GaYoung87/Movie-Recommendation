from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.views.decorators.http import require_POST, require_GET

# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    print(Movie.objects.all())
    print(movies, 'movies')
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/create.html', context)



def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm()
    context = {'movie': movie, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'movies/detail.html', context)


def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form': form, 'movie': movie}
    return render(request, 'movies/update.html', context)


def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


def reviews(request, movie_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie_id = movie_pk
        comment.save()
    return redirect('movies:detail', movie_pk)
