from bs4 import BeautifulSoup
import urllib.request as req

url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

#ulropen()으로 데이터 가져오기
res= req.urlopen(url)

#beautifulsoup으로 분석하기
soup= BeautifulSoup(res,"html.parser")

#원하는 데이터로 추출하기
title=soup.find("title").string
wf=soup.find("wf").string
print(title)
print(wf)
