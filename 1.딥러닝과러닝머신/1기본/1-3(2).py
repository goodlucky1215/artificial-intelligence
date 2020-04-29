from bs4 import BeautifulSoup
fp= open("books.html",encoding="utf-8")
soup=BeautifulSoup(fp, "html.parser")

#books,htmㅣ 과 묶음

#CSS 선택지로 검색하는 방법(10가지)
sel= lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")
sel(soup.select("li")[3].string) # 왜 
sel(soup.find_all("li")[3].string) # 안돼냐...ㅠㅠ
