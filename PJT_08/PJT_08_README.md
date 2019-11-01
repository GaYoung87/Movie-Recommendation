# PJT_08

### 1. 데이터베이스 설계

- Movies, Genres, Reviews

```python
from django.db import models
from django.conf import settings

# model은 무조건 단수!
# Genre
class Genre(models.Model):
    name = models.CharField(max_length=20)

# Movie
class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

# Review
class Review(models.Model):
    content = models.CharField(max_length=80)
    score = models.IntegerField()
    #  알아서 db에 movie_id로 저장시킨다.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```



### 2. Seed Data 반영

- 주어진 movie.json 과 genre.json 을 movies/fixtures/ 디렉토리로 옮긴 후

  `python manage.py loaddata genre.json`, `python manage.py loaddata movie.json`로 반영

- admin.py 에 Genre 와 Movie 클래스를 등록한 후, /admin 을 통해 실제로 데이터베이스에 반영
  되었는지 확인

```python
from django.contrib import admin
from .models import Genre, Movie, Review

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
```



### 3. movies앱에서 api 요청보낼 수 있는 서버 구축

- 허용된 HTTP 요청을 제외하고는 모두 405 Method Not Allowed를 응답

**pjt_08의 url**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # API 요청을 보내는 서버가 GET/api/v1/genres/이므로 
    path('api/v1/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
```



**models.py**

```python
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
```



**serializers.py**

- 장고에 orm이라는 것은 db에서 data를 꺼내서 장고에 꺼내는 역할
- 장고에 orm은 장고만 알고있는 특정 자료구조.(객체) 그걸 그래도 요청에 담아서 사용자에게 응답을 보내면 사용자는 웹페이지만 가지고있지, 장고를 해석할 수 없다.
- 이 데이터를 브라우저에서 해석할 수 있도록 데이터를 변환시키게하는 것.
- ex. 가장 대표적인 JSON타입으로 변환시켜주는 것

```python
from rest_framework import serializers
from .models import Genre, Movie, Review

# 장고에 orm이라는 것은 db에서 data를 꺼내서 장고에 꺼내는 역할
# 장고에 orm은 장고만 알고있는 특정 자료구조.(객체) 그걸 그래도 요청에 담아서 사용자에게 응답을 보내면
# 사용자는 웹페이지만 가지고있지, 장고를 해석할 수 없다.
# 이 데이터를 브라우저에서 해석할 수 있도록 데이터를 변환시키게하는 것.
# JSON타입으로 변환시켜주는 것

# Genre
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', )

# Movie
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id', )


# 특정 장르에 대한 영화를 보여준다
class GenreDetailSerializer(GenreSerializer):
    # 영화에 대한 정보들을 가지고와서
    movies = MovieSerializer(many=True)

    class Meta(GenreSerializer.Meta):
        # 장르 필드 뒤로 붙여준다.
        fields = GenreSerializer.Meta.fields + ('movies', )
# 모델에 가서보면, Movie 모델에는 genre가 있지만, Genre모델에는 그에 따른 movie정보가 없다 따라서 movie.genre가 genre.movie가 될 수 있게 related_name을 이용한다.


# Review
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie_id', 'user_id', )
```



**urls.py**

```python
# ulrs.py
from django.urls import path, include
from . import views
# app_name은 지금 당장 사용하지 않음
# 이것은 {{ movies:detail }}과 같을 때 사용!
app_name = 'movies'
urlpatterns = [
    # GET/api/v1/genres/
    path('genres/', views.genre_list, name='genre_list'),
    # GET/api/v1/genres/{genre_pk}/
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    # GET/api/v1/movies/
    path('movies/', views.movie_list, name='movie_list'),
    # GET/api/v1/genres/{movie_pk}
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # POST/api/v1/movies/{movie_pk}/reviews/
    path('movies/<int:movie_pk>/reviews/', views.review_create, name='review_create'),
    # PUT/api/v1/reviews/{review_pk}/
    # DELETE/api/v1/reviews/{review_pk}/
    path('reviews/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
]
```

```python
# views.py
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, GenreDetailSerializer
from .models import Genre, Movie, Review
from rest_framework.response import Response 

# GET/api/v1/genres/
@api_view(['GET'])
def genre_list(request):
    # 장르의 모든 정보를 가지고온다
    genres = Genre.objects.all()
    # 모든 장르를 가지고온다
    serializer = GenreSerializer(genres, many=True)
    # 장르에 대한 데이터를 보여준다
    return Response(serializer.data)


# GET/api/v1/genres/{genre_pk}/
@api_view(['GET']) # 단순 정보요청: get
def genre_detail(request, genre_pk):
    # 없는 경로 변수(genre_pk)로 접근하는 경우 404 Not Found 에러를 응답
    genre = get_object_or_404(Genre, pk=genre_pk)
    # 장르에 대한 영화(스릴러 장르의 영화 보여주기!)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


# GET/api/v1/movies/
@api_view(['GET'])
def movie_list(request):
    # 영화에 대한 모든 정보를 가지고와라
    movies = Movie.objects.all()
    # 모든 영화에 대한 정보를 가지고와라
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    


# GET/api/v1/genres/{movie_pk}/
@api_view(['GET'])
def movie_detail(request, movie_pk):
    # 없는 경로 변수(genre_pk)로 접근하는 경우 404 Not Found 에러를 응답
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 하나의 영화에 대한 정보를 보여줘라
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# POST/api/v1/movies/{movie_pk}/reviews/
@api_view(['POST'])
def review_create(request, movie_pk):
    # 사용자가 요청한 것의 데이터를 리뷰에서 가지고와라
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  
        # 검증에 실패하면 400 Bad request 오류를 발생
        # raise_exception: valid하지 않으면 예외처리하겠다는 의미
        serializer.save(movie_id=movie_pk, user_id=request.user.pk)  
        # ReviewSerializer에 movie_id, user_id가 있기 때문에
        # request.user -> gayoung, request.user.pk=1
    return Response({"message": "작성되었습니다."})



# PUT/api/v1/reviews/{review_pk}/
# DELETE/api/v1/reviews/{review_pk}/
@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    # 없는 경로 변수(genre_pk)로 접근하는 경우 404 Not Found 에러를 응답
    review = get_object_or_404(Review, pk=review_pk)
    # method == 'PUT'인 경우
    if request.method == 'PUT':
        # Review에서 데이터를 가지고오는데, 기존 저장된 내용 자체를 가지고와라
        serializer = ReviewSerializer(data=request.data, instance=review)
        # serializer가 형식에 맞으면 저장하고, 수정되었다고 알려줘라
        # 데이터 수정은 postman 들어가서 하고, 확인은 db로 하기!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "수정되었습니다."})
	# method == 'DELETE'인 경우
    else:
        review.delete()
    return Response({"message": "삭제되었습니다."})
```

****

**GET/api/v1/genres/**

![image-20191101172705040](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101172705040.png)

**GET/api/v1/genres/{genre_pk}/**

![image-20191101172858988](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101172858988.png)

**GET/api/v1/movies/**

![image-20191101172927734](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101172927734.png)

**GET/api/v1/genres/{movie_pk}/**

![image-20191101173034512](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101173034512.png)

**POST/api/v1/movies/{movie_pk}/reviews/**

![image-20191101173052014](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101173052014.png)

**PUT/api/v1/reviews/{review_pk}/**

**DELETE/api/v1/reviews/{review_pk}/**

![image-20191101173153714](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191101173153714.png)

