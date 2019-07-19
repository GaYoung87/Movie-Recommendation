import requests
from pprint import pprint
from datetime import datetime, timedelta # 요청을 보낼 때 시간정보를 계속 바꿔가면서 보내야함
from decouple import config




targetDt = datetime(2019, 7, 13) - timedelta(weeks=50)
targetDt = targetDt.strftime('%Y%m%d') # yyyymmdd

key = config('API_KEY')
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'

response = requests.get(api_url) # 브라우저에서 가장 아래 예시요청 엔터치는 것고 같음
data = response.json()  # 보기 편하게

pprint(data)