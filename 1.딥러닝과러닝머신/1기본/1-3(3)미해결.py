
from bs4 import BeautifulSoup
fp=open("fruits-vegetables.html", encoding="utf-8")
soup=BeautifulSoup(fp,"html.parser")

#CSS로 추출하기
try:
    print(soup.select_one("li:nth-of-type(8)").string)
except:
    df=""
    print(df)



      
