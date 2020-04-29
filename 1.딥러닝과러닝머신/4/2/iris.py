import pandas
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pandas.read_csv("iris1.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

#train_test_split()는 학습 전용 데이타와 테스트 전용 데이터로 나눔.
#알아서 train 과 test로 나눠준다;
train_data, test_data, train_label, test_label = \
            train_test_split(data, label)

#데이터 학습시키기(외우기)
clf = svm.SVC()
clf.fit(train_data,train_label) #fit은 학습 기계에 데이터를 학습
results = clf.predict(test_data) #predict 데이터를 넣어 예측

#test_label이 results와 얼마나 맞냐를 통해서 정답률 예측
score = metrics.accuracy_score(results, test_label)
print("정답률=",score)
