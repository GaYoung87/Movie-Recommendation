### pjt_06 하고나서(modelform 작성한 경우만!) Bootstrap사용하기

1. 가상환경 잡기

2. pip install django-bootstrap

3. installed_apps에 'django-extensions', 밑에 'bootstrap4'사용

4. base.html에서 title바로위에 -> {% bootstrap_css %}

   ​						container바로 아래 -> {% bootstrap_javascript jquery='full '%}

5. create.html에서(html마다 적용!)

   -  {% load bootstrap4 %}

   -  {{ form.as_p }}랑 button지우고 

   - {% bootstrap_form form layout='horizontal' %}

     {% buttons submit="생성하기" reset="취소" %}{% endbuttons %}

