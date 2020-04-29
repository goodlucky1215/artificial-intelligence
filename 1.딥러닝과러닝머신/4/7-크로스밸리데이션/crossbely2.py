import pandas as pd
from sklearn import svm,metrics, model_selection
from sklearn.model_selection import GridSearchCV

#MNIST 학습 데이터 읽어 들이기
train_csv = pd.read_csv("./mnist/train.csv")
test_csv  = pd.read_csv("./mnist/t10k.csv")

#필요한 열 추출하기
train_label = train_csv.ix[:,0]
train_data = train_csv.ix[:,1:577]
test_label = test_csv.ix[:,0]
test_data = test_csv.ix[:,1:577]
print("학습 데이터의 수=", len(train_label))

#그리드 서치 매개변수 설정
params = [
    {"C":[1,10,100,1000], "kernel":["linear"]},
    {"C":[1,10,100,1000], "kernel":["rbf"], "gamma":[0.001,0.0001]}
]

#그리드 서치 수행 - 각 매개변수를 적당한 범위 내부에서 변경하면서 가장 성능이 좋은 값을 찾는 방법이다.
clf = GridSearchCV(svm.SVC(),params,n_jobs=-1) #n_jobs은 병렬 계산할 프로세스 수를 지정할 수 잇다. 이를 -1로 지정하면 자동으로 코어의 수에 맞게 프로세스 수를 정해준다.
clf.fit(train_data, train_label)
print("학습기=",clf.best_estimator_)


#테스트 데이터 확인하기
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print("정답률=",ac_score)
