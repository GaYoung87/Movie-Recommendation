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























