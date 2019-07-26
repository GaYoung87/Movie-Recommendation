# Project 02

## 1번: 지난 프로젝트에서 얻은 영화명(국문)을 바탕으로 추가적인 데이터 수집

```python
import requests  # 요청하기 위한 모듈
import time  # 시간 관리위한 모듈
from pprint import pprint
import csv
# time.sleep(0.2) # 코드요청응답시 속도 늦추기(너무 빠르면 naver에서 안해줌)

# web에는 크게 header, data. 요청을 보낼 때 정보들을 넣어서 전달해줌
# 헤더: 요청에 대한 정보가 담겨져 있는 곳, 데이터: 데이터를 담을 수 있는 공간

base_url = 'https://openapi.naver.com/v1/search/movie.json'

CLIENT_ID = 'IHEQsOEdrFdEufvlc6J0'
CLIENT_SECRET = 'qEmtqe4GCi'

HEADERS = {
    'X-Naver-Client-Id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_SECRET,
}

with open('movie.csv', 'r', encoding='utf-8') as f:
 		   					# 지난번 저장 파일 PJT02로 가지고와서 저장
    movies = csv.DictReader(f)  # DictReader로 읽기! (그냥 reader쓰면 list로 받음)
    result = {}  
    	 # 최종적으로 필요한 정보만을 담을 딕셔너리 만들기(key는 영화명 why? 영화명을 통해 요청하기 때문!)
    for movie in movies:  # movies에서 영화를 읽어와 제목마다 dict로 표현
        code = movie['movieCd']  # 내용저장시 movie.csv에 있는 영화 대표코드가 필요하기 때문
        name = movie['movieNm']  # name 변수에 넣지 않고 api 주소에다가 쓰면 안됨! why? f-string내에서는 ''를 사용할 수 없음
        api_url = f'{base_url}?query={name}'  # 영화명으로 요청하기 때문
        response = requests.get(api_url, headers=HEADERS).json()
        # pprint(response)
        for k in range(response['display']): # <1번 이슈>
            time.sleep(0.1)
            # print(response['items'][k]['image'])
            if movie['directors'] in response['items'][k]['director']: # <2번 이슈>
                moive_dict = {'movieCd': code, 'link': response['items'][k]['link'], 'image': response['items'][k]['image'], 'userRating': response['items'][k]['userRating']}  
                			# movie_dict에 우리가 뽑아내고 싶은 데이터의 이름을 제시한다(이름: 데이터)
                # print(movie['directors'])
                result[movie['movieNm']] = moive_dict  # 영화명을 기준으로 딕셔너리를 만든다.
                time.sleep(0.1)
                # print(name)
    # pprint(result)
```

1. 1번 이슈

```python
for k in range(response['display']):
```

- 원래 'display'자리에 'items'를 넣었는데 돌아가다가 KeyError이 뜨는 경우 있었기 때문에 value값이 숫자 하나로 이루어진 display를 씀.

- 응답받은 것(dict 안에 dict있음)에서 영화 제목에 따른 갯수를 세고 싶었기 때문에 for문을 작성함. (영화 제목 하나에 여러 영화가 출력된 경우도 있음)



2. 2번 이슈

```python
if movie['directors'] in response['items'][k]['director']:
```

- 영화 제목을 기준으로 데이터를 뽑아내니, 같은 제목의 영화가 여러가지가 나왔음. 그 중 우리가 찾는 영화를 뽑기 위해 감독의 이름 확인해봄.

- response의 item으로 들어가 몇번째 영화인지 보고 그 영화의 감독 중 csv에 있는 감독이름이 포함되어있다면 그 데이터를 뽑는다.(csv에는 한명의 감독, response에는 여러명의 감독이 적혀있는 경우 있었음)

  

3. 결과

   ![1564123946372](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564123946372.png)
   



## 2번 : 영화 포스터 이미지 저장

```python
import requests
import csv
from pprint import pprint
import time

with open('movie_ans.csv', 'r', newline='', encoding='utf-8') as f:
		# 1번에서 작성한 movie_ans.csv에서 문서를 읽어옴 
    items = csv.DictReader(f)  # 데이터들을 items으로 가지고 오기

    for item in items:  # items들을 하나씩 뽑아올 때
        image_url = item['image']  # 이미지url을 뽑아오고
        movie_code = item['movieCd']  
        		# 영화코드를 뽑아옴 -> 이렇게 따로 movie_code라는 변수를 만들어주는 이유는 f-string안에서는 item['movieCd']('')를 사용하지 못하기 때문

        with open(f'images/{movie_code}.jpg', 'wb') as f: #wb = write binary
            	# 영화명(영화코드) 별로 이미지를 저장해와야하기 때문에 with open을 for문 안에다 사용해 이미지를 불러온다.
            response = requests.get(image_url)
            # print(movie_code)
            f.write(response.content)
```

