from bs4 import BeautifulSoup
import urllib.request


url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml,"html.parser")
seoul=soup.find_all("location")[0]
dates = seoul.find_all("data")
for item in dates:
    print(item.find("tmn").text)
