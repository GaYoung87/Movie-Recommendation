# PJT05 : Django

### 1. Django 프로젝트 시작
------

```bash
$ venv
$ python -V
$ pip list
$ python -m pip install --upgrade pip
$ pip install django
$ python -m venv venv
$ pip install django
# bash 끄고 다시 시작
```



### 2. Django 프로젝트 생성

------

- django-admin 명령어를 통해 프로젝트를 시작하고 manage.py로 앱 생성

```bash
$ django-admin startproject crud .

$ python manage.py startapp movies
```



- settings.py의 INSTALLED_APPS에 만든 앱 등록

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

<br/>

- TEMPLATES 변수의 'DIRS'에 base.html의 경로 등록

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

<br />

- 앞으로 작성하게 될 html 파일들의 기본 템플릿을 base.html에 작성

```django
{% comment %} crud 안에 templates를 만들어서 그 안에 base.html 생성 {% endcomment %}
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



### 3. model을 구축하기

- models.py에 Movie 모델과 속성 생성

```python
# crud - models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_data = models.DateTimeField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

- makemigrations, migrate를 통해 Django에 모델이 작성되었음을 선언

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br/>

- admin.py에 Movie클래스를 import한 뒤 admin.site 등록

```python
# admin.py
# admin을 생성해주면 굳이 SQLite3에서 INSERT INTO를 하나하나 입력할 필요 없이, 해당 사이트에서 입력해도 데이터가 생성됨
from django.contrib import admin
from .models import Movie

# Register your models here.
admin.site.register(Movie)
```

- createsuperuser를 통해 관리자 계정 생성

```bash
$ python manage.py createsuperuser
```

- crud - urls.py에 movies에 작성한 것들은 movies.url로 들어감을 나타냄
- 여러 앱들이 만들어지고, 그에 따라 여러 모델들이 들어가게 될때, 특정 앱을 지정하지 않는다면 templates, urls, views에서 서로 섞여 원하는 정보를 볼 수 없음

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
```

<br/>

- settings.json에서 django앱 관련된 것 붙이기

```python
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    
    "emmet.includeLanguages": {"django-html": "html"},
}
```



### 4. 영화 정보 데이터 관리를 위한 페이지 작성

---------

##### 1) 영화목록 :  Index

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
```

```django
{% comment %} index.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 목록{% endblock title %}

{% block body %}
<a class="ml-2" href="/movies/new/">새 영화 등록</a><hr>
{% for movie in movies %}
<p><a class="ml-2" href="/movies/{{ movie.pk }}/">{{ movie.title }}</a>: {{ movie.score }}</p>
{% endfor %}
{% endblock body %}
```

![index page](C:\Users\student\Desktop\index.PNG)

##### 2) 영화 정보 생성 Form :  new

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

def new(request):
    return render(request, 'movies/new.html')
```

```django
{% comment %} new.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 생성 Form{% endblock title %}

{% block body %}
<h1>영화 정보 생성</h1>

<form action="/movies/create/">
<label for="title">영화명</label><br>
<input type="text" id="title" name="title"><br><br>

<label for="title_en">영화명(영문)</label><br>
<input type="text" id="title_en" name="title_en"><br><br>

<label for="audience">누적 관객수</label><br>
<input type="number" id="audience" name="audience"><br><br>

<label for="open_data">개봉일</label><br>
<input type="date" id="open_data" name="open_data"><br><br>

<label for="genre">장르</label><br>
<input type="text" id="genre" name="genre"><br><br>

<label for="watch_grade">관람등급</label><br>
<input type="text" id="watch_grade" name="watch_grade"><br><br>

<label for="score">평점</label><br>
<input type="number" id="score" name="score"><br><br>

<label for="poster_url">포스터 이미지 URL</label><br>
<input type="text" id="poster_url" name="poster_url"><br><br>

<label for="description">영화 소개</label><br>
<textarea name="description" id="description" cols="30" rows="10"></textarea><br><br>

<button type="submit">[생성하기]</button>
</form>

{% endblock body %}
```

![1569289614256](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569289614256.png)

##### 3) 영화 정보 생성 : create

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

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
```

```django
{% comment %} create.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 생성{% endblock title %}

{% block body %}
<h3>영화 정보 생성이 완료되었습니다.</h3>
<p><a href="/movies/">영화 목록으로 이동</a></p>
{% endblock body %}
```

![1569289895893](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569289895893.png)



##### 4) 영화 정보 조회 : detail

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
```

```django
{% comment %} detail.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 조회{% endblock title %}

{% block body %}

    <p>영화명: {{ movie.title }}</p>
    <p>영화명(영문): {{ movie.title_en }}</p>
    <p>누적 관객수: {{ movie.audience }}</p>
    <p>개봉일: {{ movie.open_data }}</p>
    <p>장르: {{ movie.genre }}</p>
    <p>관람등급: {{ movie.watch_grade }}</p>
    <p>평점: {{ movie.score }}</p>
    <p>포스터 이미지 URL: {{ movie.poster_url }}</p>
    <p>영화 소개: {{ movie.description }}</p>

    <a href="/movies/">목록</a>
    <a href="/movies/{{ movie.pk }}/edit/">수정</a>
    <a href="/movies/{{ movie.pk }}/delete/">삭제</a>

{% endblock body %}
```

![1569289993080](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569289993080.png)

##### 5) 영화 정보 수정 Form : edit

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    open_data = movie.open_data
    open_data = open_data.strftime("%Y-%m-%d")  # 시간 표시 방법 지정!
    context = {
        'movie': movie,
        'open_data': open_data,
    }

    return render(request, 'movies/edit.html', context)
```

```django
{% comment %} edit.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 수정 Form{% endblock title %}

{% block body %}
<h1>영화 정보 수정</h1>

<form action="/movies/{{ movie.pk }}/update/">
<label for="title">영화명</label><br>
<input type="text" id="title" name="title">{{ movie.title }}<br><br>

<label for="title_en">영화명(영문)</label><br>
<input type="text" id="title_en" name="title_en">{{ movie.title_en }}<br><br>

<label for="audience">누적 관객수</label><br>
<input type="number" id="audience" name="audience">{{ movie.audience }}<br><br>

<label for="open_data">개봉일</label><br>
<input type="date" id="open_data" name="open_data">{{ movie.open_data }}<br><br>

<label for="genre">장르</label><br>
<input type="text" id="genre" name="genre">{{ movie.genre }}<br><br>

<label for="watch_grade">관람등급</label><br>
<input type="text" id="watch_grade" name="watch_grade">{{ movie.watch_grade }}<br><br>

<label for="score">평점</label><br>
<input type="number" id="score" name="score">{{ movie.score }}<br><br>

<label for="poster_url">포스터 이미지 URL</label><br>
<input type="text" id="poster_url" name="poster_url">{{ movie.poster_url }}<br><br>

<label for="description">영화 소개</label><br>
<textarea name="description" id="description" cols="30" rows="10">{{ movie.description }}</textarea><br><br>

<button type="submit">[수정하기]</button>
</form>

{% endblock body %}
```

![1569290253377](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569290253377.png)

##### 6) 영화 정보 수정 : update

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

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
```

```django
{% comment %} update.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 수정{% endblock title %}

{% block body %}
<h3>영화 정보 수정이 완료되었습니다.</h3>
<p><a href="/movies/">영화 목록으로 이동</a></p>
{% endblock body %}
```

![1569290987451](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569290987451.png)

##### 7) 영화 정보 삭제 : delete

```python
# views.py
from django.shortcuts import render, redirect
from .models import Movie
from datetime import datetime

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return render(request, 'movies/delete.html')
```

```django
{% comment %} delete.html {% endcomment %}
{% extends 'base.html' %}

{% block title %}영화 정보 삭제{% endblock title %}

{% block body %}
<h3>영화 정보 삭제가 완료되었습니다.</h3>
<p><a href="/movies/">영화 목록으로 이동</a></p>
{% endblock body %}
```

![1569290666505](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569290666505.png)