from urllib.parse import urljoin

base="http://example.com/html/a.html"

print(urljoin(base,"b.html"))
print(urljoin(base,"sub/c.html"))
print(urljoin(base,"../index.html"))
print(urljoin(base,"../img/hoge.png"))
print(urljoin(base,"../css/hoge.css"))

print(urljoin(base,"/hoge.html"))
print(urljoin(base,"http://otherExample.com/wiki")) # http://등으로 시작한다면
print(urljoin(base,"//anotherExample.org/test")) #앞에꺼 무시하고 이걸로 동작
