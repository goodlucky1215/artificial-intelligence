import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

file = codecs.open("2BEXXX01.txt","r",encoding="utf-16")
#html.parser로 파일을 분석
soup = BeautifulSoup(file, "html.parser")
#body에서 text를 가져온다는 의미
body = soup.select_one("text > body")
text = body.getText()
#print(text)

twitter = Twitter()
word_dic = {}
#text를 한 줄씩 분할해서 읽음
lines = text.split("\r\n")

#형태소 중에서 명사만이 몇 번 등장하는 지 알려주는 방법
for line in lines:
    malist = twitter.pos(line)
    #print(malist) 하면 형태소 분석과 품사를 알 수 있게 보여줌. 
    #break    
    for taeso, pumsa in malist:
        if pumsa == "None":
        #taeso(형태소)가 만약에 품사(pumsa)가 "None" 즉 명사라면,
            if not (taeso in word_dic):
            # word_dic 안에 그 형태소가 저장돼 있지 않다면,
                word_dic[taeso] = 0
                #처음에는 그 형태소가 0 이라는 값으로 저장됐다가,
            word_dic[taeso] += 1
            # +1로 횟수 저장됀다. 만약에 이미 word_dic 안에 저장된 형태소라면,
            # 바로 +1이 더 저장돼겠지!!!!
#print(word_dic)

#형태소 중에서 명사들 중에서 많이 등장하는 형태소와 수 켜기
#sorted는 횟수 순서대로 정렬하는데 reverse=True를 사용해서 큰 수부터 정렬함.
#temp = lambda x: x # 아래와 용도가 같습니다===> def temp(x): return x
#즉, key=lamda x:x[1]이므로 즉 그 형태소의 횟수로 sorted(정렬)시킨다는 의미!
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
#50번째까지만 형태소 이름과 횟수를 뽑아낸다.
for word, count in keys[:50]:
    print("{0}({1}) ".format(word,count),end="") #format을 쓰면 {0}({1})순서대로 값들을 알려줌.
print()
 
