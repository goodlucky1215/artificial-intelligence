#라이브러리 읽어 들이기
from bs4 import BeautifulSoup

#분석하고 싶은 HTML
html="""
<html><body>
 <ul>
   <li><a href= "http://www.naver.com">naver</a><li>
   <li><a href= "http://www.daum.net">daum</a><li>
 <ul>  
</body></html>
"""


# HTML 분석하기
soup = BeautifulSoup(html,'html.parser')


#find_all() 메서드로 추출하기-find_all은 a 태그를 추출
links = soup.find_all("a")


#링크 목록 출력하기기
for a in links:
    href = a.attrs['href']
    text=a.string
    print(text,">",href)


#여기서부터는 shell에 검색
#분석 잘 됐는지 확인하기
a=soup.p.a


#<a> 태그를 변수 a에 할당
a=soup.p.a


#attrs 속성의 자료형 확인
type(a.attrs)


#href속성이 있는지 확인
'href' in a.attrs


#href 속성값 확인
a['href']
