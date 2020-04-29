def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r

a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."

#2-gram
r2, word2 = diff_ngram(a,b,2)
#ngram(a, 2): --> res = [] --> slen = len(s) - 2 + 1 = 22-2+1 =19
#ss = s[0:2]  --> res.append(ss) --> res = ['오늘']
#ss = s[1:3]  --> res.append(ss) --> res = ['오늘',늘 ']
#이런식으로하면,
# a = ['오늘', '늘 ', ' 강', '강남', '남에', '에서', '서 ', ' 맛', '맛있', '있는',
#'는 ', ' 스', '스파', '파게', '게티', '티를', '를 ', ' 먹', '먹었', '었다', '다.']
# b = ['강남', '남에', '에서', '서 ', ' 먹', '먹었', '었던', '던 ', ' 오', '오늘', '늘의',
#'의 ', ' 스', '스파', '파게', '게티', '티는', '는 ', ' 맛', '맛있', '있었', '었다', '다.']
# r = [] / cnt = []
#a b 의 글이 같으면 그것을 cnt에 더해서 len(a) 만큼 나눈게 확률로 돼서 r2 에 들어가고,
#r 은 글이 같은 것만 저장해서 그 글을 뽑아낸다. 그래서 그게 word2 가 됨.
print("2-gram:", r2, word2)

#3-gram
r3, word3 = diff_ngram(a,b,3)
print("3-gram:", r3, word3)
