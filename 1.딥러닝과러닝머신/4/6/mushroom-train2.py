import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#데이터 읽어들이기
mr = pd.read_csv("mushroom.csv",header=None)

#데이터 내부의 분류 변수 전개하기
label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    #row_index = 0 을 처음에 갖고 row= p (A1이 p니까)를 갖고 for col, v in enumerate(row.ix[1:]): 를 들어간다.
    label.append(row.ix[0]) 
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        #col = 0 을 처음에 갖고 enumerate(row.ix[1:])이므로 v = x (B1이 x니까) 를 갖는다.
        #row_index = 0 을 처음에 갖으므로 attr = {"dic":{},"cnt":0}로 들어가고
        #attr_list= {"dic":{},"cnt":0}가 됌.
        if row_index == 0:
            attr = {"dic":{},"cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        # 버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        # attr["dic"]={}므로 처음에 else로 들어가서
        #idx = 0 이됨. 그리고 attr["dic"][v]= idx 므로 attr["dic"] = {x : 0}이 됨.
        #attr["cnt"] += 1 므로  attr["cnt"]=1 이 된다.
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

#print(data[0:5])
#이것을 프린트하면 데이터의 크고 작음보다는 분류 변수라서
#각각의 숫자를  벡터처럼 나열 즉 예를 들면  s=00000000001 과 같이 나타나져서
#값을 가진다.(자세한 설명은 메모장을 확인해라.)

#학습 전용 데이터와 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test= \
            train_test_split(data,label)

#데이터 학습 시키기
clf = RandomForestClassifier()
clf.fit(data_train,label_train)

#데이터 예측하기
predict = clf.predict(data_test)

#결과 테스트
ac_score= metrics.accuracy_score(label_test,predict)
print("정답률=",ac_score)
