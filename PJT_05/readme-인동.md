# Project 05 : Django

<br />

### 1. Django 프로젝트를 생성하고 model을 구축하기

------

```bash
$ django-admin startproject crud .

$ python manage.py startapp movies
```

- django-admin 명령어를 통해 프로젝트를 시작하고 manage.py로 앱을 생성합니다.

<br/>

```python
INSTALLED_APPS = [
    'movies',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- settings.py의 INSTALLED_APPS에 만든 앱을 등록합니다.

  <br/>

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>{% block title %}{% endblock %}</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  {% block content %}{% endblock %}
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

- 앞으로 작성하게 될 html 파일들의 기본 템플릿을 base.html에 작성합니다. 이는 프로젝트 폴더 내의 templates/ 에 저장될 것입니다.

  <br/>

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- TEMPLATES 변수의 'DIRS'에 base.html의 경로를 등록해 줍니다.

<br />

```python
# models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- models.py에 Movie 모델과 속성을 생성합니다.
- migrations을 통해 django에 모델이 작성됐음을 선언합니다.

<br/>

```python
# admin.py

from django.contrib import admin
from .models import Movie

# Register your models here.
admin.site.register(Movie)
```

- admin.py에 Movie 클래스를 import한 뒤 admin.site를 등록합니다.
- python manage.py createsuperuser를 통해 관리자 계정을 생성합니다.

<br/>

### 2. 영화 정보 데이터를 관리하기 위한 페이지 작성

<hr/>
#### index.html

```html
{% extends 'base.html' %}

{% block title %}Article Index{% endblock %}

{% block content %}
<a class="ml-2" href="/movies/new/">새 영화 등록</a><hr/>
{% for movie in movies %}
<p><a class="ml-2" href="/movies/{{ movie.pk }}/">{{ movie.title }}</a> : {{ movie.score }}</p>
{% endfor %}
{% endblock %}
```

```python
# views.py

from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    
    return render(request, 'movies/index.html', context)
```

- views.py에 index 함수를 만들고 movies 변수에 Movie의 모든 objects를 할당합니다. 그리고 context를 통해 index.html에 전달합니다.
- index.html에서는 반복문으로 영화의 제목과 평점을 순차적으로 출력합니다. 영화 제목에는 a 태그를 넣어 영화 정보 페이지로 이동할 수 있도록 합니다.

<br/>

#### new.html

```html
{% extends 'base.html' %}

{% block title %}영화 정보 생성 Form{% endblock %}

{% block content %}
<h1 class="m-2">영화 정보 생성하기</h1><br/>
<form class="ml-3" action="/movies/create/">
<label for="title">제목</label><br/>
<input type="text" id="title" name="title"><br/><br/>

<label for="title_en">영문 제목</label><br/>
<input type="text" id="title_en" name="title_en"><br/><br/>

<label for="audience">관객수</label><br/>
<input type="number" id="audience" name="audience"><br/><br/>

<label for="open_date">개봉일</label><br/>
<input type="date" id="open_date" name="open_date"><br/><br/>
<h1>{{ movie.open_date }}</h1>

<label for="genre">장르</label><br/>
<input type="text" id="genre" name="genre"><br/><br/>

<label for="watch_grade">관람 등급</label><br/>
<input type="text" id="watch_grade" name="watch_grade"><br/><br/>

<label for="score">평점</label><br/>
<input type="number" id="score" name="score"><br/><br/>

<label for="poster_url">포스터 URL</label><br/>
<input type="text" id="poster_url" name="poster_url"><br/><br/>

<label for="description">줄거리</label><br/>
<textarea id="description" name="description" cols="30" rows="10"></textarea>><br/><br/>

<button type="submit">생성하기</button><br/>

{% endblock %}
```

#### create.html

```html
{% extends 'base.html' %}

{% block title %}Created!{% endblock %}

{% block content %}
<h1 class="text-center">영화 정보 생성이 완료되었습니다.</h1>
<p><a href="/movies/">영화 목록으로 이동하기</a></p>
{% endblock  %}
```

```python
# views.py

def new(request):

    return render(request, 'movies/new.html')


def create(request):
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date,
    genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()

    return render(request, 'movies/create.html')

```

- 영화 정보를 작성할 수 있는 new.html을 생성합니다. 하단의 생성하기 버튼을 누르면 /movies/create/로 입력된 정보를 전달할 수 있도록 합니다.
- 전달받은 정보는 view.py에서 request.GET.get을 통해 각각의 변수에 저장합니다. 이를 Movie 클래스의 인자로 전달함으로써 모델에 데이터를 등록합니다.
- 생성이 완료되면 create.html에서 이를 표시해줍니다.

<br/>

#### detail.html

```html
{% extends 'base.html' %}

{% block title %}영화 정보{% endblock %}

{% block content %}
<div class="m-2">
<p>제목 : {{ movie.title }}</p>
<p>영문 제목 : {{ movie.title_en }}</p>
<p>관객수 : {{ movie.audience }}</p>
<p>개봉일 : {{ movie.open_date }}</p>
<p>장르 : {{ movie.genre }}</p>
<p>관람 등급 : {{ movie.watch_grade }}</p>
<p>평점 : {{ movie.score }}</p>
<p>포스터 URL : {{ movie.poster_url }}</p>
<p>줄거리 : {{ movie.description }}</p>
</div>

<a class="m-2" href="/movies/">목록</a>
<a class="m-2" href="/movies/{{ movie.pk }}/edit/">수정</a>
<a class="m-2" href="/movies/{{ movie.pk }}/delete/">삭제</a>
{% endblock %}
```

```python
# views.py

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context) 
```

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]
```



- 영화 정보 조회 페이지는 /movies/ 다음에 pk(primary key)값을 입력함으로써 접근하게 됩니다. 이를 위해 urls.py에서 movie_pk를 동적으로 할당할 수 있게 만들어 줍니다.
- 이후 views.py의 detail 함수에 이를 인자로 전달합니다. pk가 movie_pk(입력받은 인자)인 objects만 movie 변수에 저장하고, context를 통해 details.html에서 이를 볼 수 있게 합니다.
- detail.html에서 {{ movie.변수명 }}을 입력하여 세부 정보를 표시합니다.
- 목록, 수정 및 삭제 페이지로 이동할 링크를 작성해둡니다.

<br/>

#### edit.html

```html
{% extends 'base.html' %}

{% block title %}영화 정보 수정 Form{% endblock %}

{% block content %}
<h1 class="m-2">영화 정보 수정하기</h1><br/>
<form class="ml-3" action="/movies/{{ movie.pk }}/update/">
<label for="title">제목</label><br/>
<input type="text" id="title" name="title" value="{{ movie.title }}"><br/><br/>

<label for="title_en">영문 제목</label><br/>
<input type="text" id="title_en" name="title_en" value="{{ movie.title_en }}"><br/><br/>

<label for="audience">관객수</label><br/>
<input type="number" id="audience" name="audience" value="{{ movie.audience }}"><br/><br/>

<label for="open_date">개봉일</label><br/>
<input type="date" id="open_date" name="open_date" value="{{ open_date }}"><br/><br/>

<label for="genre">장르</label><br/>
<input type="text" id="genre" name="genre" value="{{ movie.genre }}"><br/><br/>

<label for="watch_grade">관람 등급</label><br/>
<input type="text" id="watch_grade" name="watch_grade" value="{{ movie.watch_grade }}"><br/><br/>

<label for="score">평점</label><br/>
<input type="number" id="score" name="score" value="{{ movie.score }}"><br/><br/>

<label for="poster_url">포스터 URL</label><br/>
<input type="text" id="poster_url" name="poster_url" value="{{ movie.poster_url }}"><br/><br/>

<label for="description">줄거리</label><br/>
<textarea id="description" name="description" cols="30" rows="10">{{ movie.description }}</textarea>><br/><br/>

<button type="submit">수정하기</button>

</form>

{% endblock %}
```

#### update.html

```html
{% extends 'base.html' %}

{% block title %}Updated!{% endblock %}

{% block content %}
<h1 class="text-center">영화 정보 수정이 완료되었습니다.</h1>
<p><a href="/movies/">영화 목록으로 이동하기</a></p>
{% endblock  %}
```

```python
# views.py
from datetime import datetime

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    open_date = movie.open_date
    open_date = open_date.strftime("%Y-%m-%d")
    context = {
        'movie': movie,
        'open_date': open_date,
    }

    return render(request, 'movies/edit.html', context)


def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_date = request.GET.get('open_date')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')

    movie.save()

    return render(request, 'movies/update.html')
```

```python
# urls.py

urlpatterns = [
    path('<int:movie_pk>/update/', views.update),
    path('<int:movie_pk>/edit/', views.edit),
    path('<int:movie_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]
```

- urls.py에서 경로를 Primary Key로 동적 할당함으로써 각각의 영화 정보 수정 Form에 접근할 수 있게 만들어 줍니다.
- detail.html에서 작성했던 것과 같이 pk가 일치하는 objects를 movie 변수에 저장하고 이를 html 페이지로 이동시킵니다. open_date 변수만은 예외로 datetime 패키지의 strftime 함수를 적용하여 새로운 값에 할당합니다. 변환 없이 그대로 전달했을 시 html 페이지의 form이 이를 날짜 변수로 인식하지 못하기 때문입니다.
- 수정이 완료된 데이터는 수정하기 버튼으로 /movies/{{ movie.pk }}/update/로 전송됩니다.
- 도착한 데이터는 request.GET.get을 통해 movie 변수에 덮어씌워집니다.

<br/>

#### delete.html

```html
{% extends 'base.html' %}

{% block title %}Deleted!{% endblock %}

{% block content %}
<h1 class="text-center">영화 정보 삭제가 완료되었습니다.</h1>
<p><a href="/movies/">영화 목록으로 이동하기</a></p>
{% endblock  %}
```

```python
# views.py

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return render(request, 'movies/delete.html')
```

```python
# urls.py

urlpatterns = [
    path('<int:movie_pk>/delete/', views.delete),
    path('<int:movie_pk>/update/', views.update),
    path('<int:movie_pk>/edit/', views.edit),
    path('<int:movie_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]
```

- 할당받은 pk와 같은 objects를 불러와 이를 삭제합니다.

