import pandas as pd
from sklearn import svm,metrics, model_selection
import random, re

#붓꽃 데이터 읽기
csv = pd.read_csv('iris.csv')

#리스트를 훈련 전용 데이터로 분리
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

#크로스 밸리데이션하기
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
#model_selection.cross_val_score( 학습평가기 객체 , 훈련 전용 데이터 , 정답레이블 , cv는 몇개로 분할 할 것인지)
print("각각의 정답률=",scores)
print("평균 정답률=",scores.mean())
