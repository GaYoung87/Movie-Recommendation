import requests
import time
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

# 지난 프로젝트에서 얻은 영화명(국문) 읽어오기
with open('movie.csv', 'r', encoding='utf-8') as f:
    movies = csv.DictReader(f)
    result = {}
    for movie in movies:
        code = movie['movieCd']
        name = movie['movieNm']
        api_url = f'{base_url}?query={name}'
        response = requests.get(api_url, headers=HEADERS).json()
        # pprint(response)
        for k in range(response['display']):
            time.sleep(0.1)
            # print(response['items'][k]['image'])
            if movie['directors'] in response['items'][k]['director']:
                moive_dict = {'movieCd': code, 'link': response['items'][k]['link'], 'image': response['items'][k]['image'], 'userRating': response['items'][k]['userRating']}
                # print(movie['directors'])
                result[movie['movieNm']] = moive_dict
                time.sleep(0.1)
                # print(name)
    # pprint(result)

with open('movie_ans.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'link', 'image', 'userRating')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for w in result.values():
        writer.writerow(w)
