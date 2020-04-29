from sklearn import svm,metrics
import random, re

#붓꽃의 csv 파일 읽어 들이기
lines = open('iris.csv', 'r', encoding='utf-8').read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
f_cols = lambda li: list(map(f_tonum,li.strip().split(',')))
csv = list(map(f_cols, lines)) #lines가 f_cols가 돼서 list 형식을 csv가 됨.
del csv[0] #헤더 제거하기
random.shuffle(csv) #데이터 섞기

#데이터를 k개로 분할하기
k = 5
csvk = [ [] for i in range(k) ] #csvk = [[], [], [], [], []]
for i in range(len(csv)):
    csvk[i % k].append(csv[i]) #i=0 이면 0 % 5 나머지는 0이므로 csvk[0].append(csv[0])이 들어감.

#리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하는 함수
def split_data_label(rows):
    data = []; label = []
    for row in rows:
        data.append(row[0:4]) #csvk = [[1,2,3,4,5,56], [2,4,6,4,8,3....] 이런식으로 있으면 data=[[1,2,3,4], [2,4,6,4]....] 들어감.
        label.append(row[4])  #csvk = [[1,2,3,4,5,56], [2,4,6,4,8,3....] 이런식으로 있으면 label=[[5],[]....] 들어감.
    return (data, label)

#정답률 구하기
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    #학습시키고 정답률 구하기
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)

#K개로 분할해서 정답률 구하기
score_list = []
for testc in csvk: #csvk = [[1,2,3,4,5,56], [2,4,6,4,8,3....] 이런식으로 있으면, testcs는 처음에 [1,2,3,4,5,56]을 값으로 바꿔 안으로
    # testc 이외의 데이터를 훈련 전용 데이터로 사용하기
    trainc = []
    for i in csvk: #csvk = [[1,2,3,4,5,56], [2,4,6,4,8,3....] 이런식으로 있으면,i의 처음은 [1,2,3,4,5,56]같으므로 trainc가 값을 안 받지만, 다음인 [2,4,6,4,8,3....]부터 값을 받기 시작.
        if i != testc: trainc += i #이렇게 돼면 trainc 는 testc 에 들어가는 하나의 값csvk 만 빼고 나머지를 전부 비교 할 수 있게된다.(크로스벨리)
    sc = calc_score(testc,trainc)
    score_list.append(sc)
    
print("각각의 정답률 =", score_list)
print("평균 정답률=", sum(score_list) / len(score_list))
    
