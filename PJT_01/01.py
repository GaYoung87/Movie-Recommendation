import requests
from pprint import pprint
from datetime import datetime, timedelta # 요청을 보낼 때 시간정보를 계속 바꿔가면서 보내야함
from decouple import config
import csv

data_list = {}
for a in range(3,0,-1):
    targetDt = datetime(2019, 7, 13) - timedelta(weeks=a)
    targetDt = targetDt.strftime('%Y%m%d') # yyyymmdd

    key = config('API_KEY')
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0&'

    response = requests.get(api_url) # 브라우저에서 가장 아래 예시요청 엔터치는 것과 같음
    data = response.json()  # 보기 편하게
    movies = data['boxOfficeResult']['weeklyBoxOfficeList']
    for movie in movies:
        data_dict = {'movieCd': movie['movieCd'], 'movieNm': movie['movieNm'], 'audiAcc': movie['audiAcc']} # dictionary가 list보다 중복제거에 편하다
        data_list[movie['movieCd']] = data_dict
    print(data_list)
# dict로 해야 우리는 데이터를 최근꺼부터보기때문에 key를 영화코드로 두고하면 데이터 추가될때 중복되어도 저장되지않음
print('============================================================================================================================')
# pprint(data_list)

# dictionary는 중복이안된다. list.append(), dict.update() -> 자동적으로 최신값으로 넣어줌.
# if문을 쓰면 계속 값이 큰거로하도록 if문을 만들어야함. 그것을 안하기 위해서 날짜를 뒤집어서

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정
    fieldnames = ('movieCd', 'movieNm', 'audiAcc')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()

    # Dictionary를 순회하며 key에 맞는 value를 한 줄씩 작성한다.
    for i in data_list.values():  # 그냥 data_list하면 안됨. avengers는 키값없이 바로 name이 나오지만, boxoffice는 key값이 있어서 .values()해야지 진짜 내가 원하는 값을 가지고올 수 있음
        writer.writerow(i)
