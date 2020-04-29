from gensim.models import word2vec
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

fp=codecs.open("2BEXXX01.txt","r",encoding="utf-16")
soup = BeautifulSoup(fp,"html.parser")
body = soup.select_one("text body")
text = body.getText()

twitter = Twitter()
lines = text.split("\r\n")
results = []
for line in lines:
    r = []
    malist = twitter.pos(line, norm=True, stem=True)
    for (word, pumsa) in malist:
        if not word in ["Josa","Eomi","Punctuation"]:
            r.append(word)
    #print(r)
    #break
    results.append((" ".join(r)).strip()) 

output = (" ".join(r)).strip()
#print(output)


with open("toji.wakati","w",encoding="utf-8") as fp:
    fp.write(output)

data = word2vec.LineSentence("toji.wakati")
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")


