import requests
import csv
from pprint import pprint
import time

with open('movie_ans.csv', 'r', newline='', encoding='utf-8') as f:
    items = csv.DictReader(f)

    for item in items:
        image_url = item['image']
        movie_code = item['movieCd']

        with open(f'images/{movie_code}.jpg', 'wb') as f: #wb = write binary  # test 말고 영진위 영화코드
            response = requests.get(image_url)
            print(movie_code)
            f.write(response.content)

