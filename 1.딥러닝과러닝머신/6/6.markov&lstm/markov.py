import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import urllib.request
import os, re, json, random

# 마르코프 체인 딕셔너리 만들기
def make_dic(words):
    tmp = ["@"]
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3 : continue
        if len(tmp) > 3 : tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic
#ex) 개|도|닷새|가|되면|주인|을|안다

# tmp = ["@","개","도"]
#w1: @ / w2: 개 / w3: 도
#dic[@][개][도] += 1 이 돼서, 다음과 같이 넣어짐.
## dic = {
#       "@": {
#           "개": {
#               "도": 1
#            }
#        }
#    }

#tmp = ["개', "도", "닷새"]
#len(tmp) > 3 일땐 tmp = tmp[1:] 가 돼기 때문에 앞자리로 땅겨짐.
# dic = {
#       "@": {
#           "개": {
#               "도": 1
#            }
#        }
#       "개": {
#           "도": {
#               "닷새": 1
#            }
#        }
#    }

#--------> 이런 식으로 만들어져서

# word가 "."까지 오면 if word == ".":
#tmp = ["@"] 가 돼서 한 문장이 끝이 난다.  


# 딕셔너리에 데이터 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1] : dic[w1][w2] = {}
    if not w3 in dic[w1][w2] : dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 문장 만들기
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    w1 = word_choice(top)     #랜덤으로 단어를 뽑는데 만약 '개'를 뽑으면
    w2 = word_choice(top[w1])#'개' 밑에 있는 애들 중에서 랜덤으로 뽑는다. 만약 '도' 가 뽑혔다면?
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2]) #이는 "닷새"를 부르게 한다.
        ret.append(w3)
        if w3 == ".": break 
        w1, w2 = w2, w3 #그리고 다시 w1 이 '도' w2 가 '닷새'를 가지면 w3은 '가'를 뽑음
    ret = "".join(ret)
    #띄어쓰기
    params = urllib.parse.urlencode({
        "_callback": "",
        "q": ret
    })
    #네이버 맞춤법 검사기를 사용합니다.
    data = urllib.request.urlopen("https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?" + params)
    data = data.read().decode("utf-8")[1:-2]
    data = json.loads(data)
    data = data["message"]["result"]["html"]
    data = soup = BeautifulSoup(data, "html.parser").getText()
    #리턴
    return data
    
def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

#문장 읽어 들이기
toji_file = "toji.txt"
dict_file = "markov-toji.json"
if not os.path.exists(dict_file):
    # 토지 텍스트 파일 읽어 들이기
    fp = codecs.open("2BEXXX01.txt", "r", encoding="utf-16")
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("text > body")
    text = body.getText()
    text = text.replace("…","") # 현재 koNLPy가 …을 구두점으로 잡지 못하는 문제 임시 해결
    #형태소 분석
    twitter = Twitter()
    malist = twitter.pos(text, norm=True)
    words = []
    for word in malist:
        # 구두점 등은 대상에서 제외(단 마침표는 포함)
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file,"w",encoding="utf-8"))
else:
    dic = json.load(open(dict_file, "r"))
# 문장 만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("---")
