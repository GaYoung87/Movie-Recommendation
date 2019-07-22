import requests  # 요청을 보내기 위한 모듈 호출
from pprint import pprint

base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
key = 'fb674af3a72ab0dd8127f928ac11daaf'  # 발급받은 API KEY
targetDt = '20190713'  #명세서 기준일
api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0&'

response = requests.get(api_url).json()  # 응답받은 결과가 json type이므로 dict 타입으로 바꾼다
pprint(response)