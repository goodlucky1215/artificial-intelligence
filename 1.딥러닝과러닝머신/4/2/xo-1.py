from sklearn import svm, metrics

data = [[0,0],[1,0],[0,1],[1,1]]
labels = [0,1,1,0]

examples = [[0,0],[1,0]]
examples_label = [0, 1]

#데이터 학습시키기(외우기)
clf = svm.SVC()
clf.fit(data,labels) #fit은 학습 기계에 데이터를 학습
results = clf.predict(examples) #predict 데이터를 넣으면 나와야할 결과 값을 알려줌.
print(results)

score = metrics.accuracy_score(examples_label,results)
print("정답률=",score)
