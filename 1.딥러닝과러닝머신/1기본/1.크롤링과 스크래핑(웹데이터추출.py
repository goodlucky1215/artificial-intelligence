import sys
import urllib.request
import urllib.parse  #as paramas 을 덧붙이면 앞에 urllib. 을 붙이지 않고 사용가능


#명령줄 매개변수 추출
if len(sys.argv)<=1:
    print("USAGE: download-forecast-argv <region number>")
    sys.exit()
regionNumber = sys.argv[1]


#매개변수 url 인코딩
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values={
     'stnId': regionNumber
}
paramas=urllib.parse.urlencode(values)

#요청 전용 url을 생성
url = API + "?" + paramas
print("url=",url)

#다운로드
data=urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
