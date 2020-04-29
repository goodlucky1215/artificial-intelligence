from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

#키 몸무게 데이터 읽기
tbl=pd.read_csv("bmi.csv")

#열을 자르고 정규화(벡터라 0~1 사이로 변환)하기
label = tbl["label"]
w=tbl["weight"] /100
h=tbl["height"] /200
wh=pd.concat([w,h],axis=1) #axis=1,0은 행과 열이랑 관련 돼 있는데 이해가 덜....

#학습 전용 데이터와 테스트 전용 데이터 나누기
data_train, data_test, lable_train, label_test = \
            train_test_split(wh, label)

#데이터 학습하기
clf=svm.SVC()
clf.fit(data_train, lable_train)

#데이터 예측하기
predict = clf.predict(data_test)

#결과 테스트
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("확률:",ac_score)
print("report:\n",cl_report)
