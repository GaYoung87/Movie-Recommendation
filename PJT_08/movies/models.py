from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    # related_name을 해야 장르가 영화에 대한 정보를 가지고올 수 있다. 
    # related_name을 쓰지않고 genre.movie를 가지고오려면 movie_set하면 된다
    # Movie.genre는 가지고올 수 있음 why? 모델안에 존재하기 때문!
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')


class Review(models.Model):
    content = models.CharField(max_length=80)
    score = models.IntegerField()
    #  알아서 db에 movie_id로 저장시킨다.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movies')