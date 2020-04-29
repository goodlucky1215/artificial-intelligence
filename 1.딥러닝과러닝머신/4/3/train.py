from sklearn import model_selection, svm, metrics

#CSV파일 읽고 가공하기
def load_csv(fname):                 #def를 이용해서 load_csv(fname)를 만듬
    labels = []                          
    images = []
    with open(fname, "r") as f:      #with는 열고 닫는 역할 해줌,fname을 "r"로 읽음 => f가 담음.
        for line in f:               #f를 line으로 하나씩 넣어줌  
            cols = line.split(",")   # ','에 따라서 각자를 분리 시켜 줌.
            if len(cols) < 2: continue #len이 길이므로 0, 1 애들은 실행돼고 2부터는 continue를 만나 위로 다시 ***그러나 여기서 cols로 인해서 0번째가 없어져서 새로운애가 계속 0번째가 됨.
            labels.append(int(cols.pop(0))) #pop(0) 0번째 애를 제거해줌 -> label에 0번쨰 애가 들어감. 
            vals = list(map(lambda n: int(n) / 256, cols)) #map의 역할로 인해서, cols가 n으로 들어감. lambda로 인해서 int(n)으로 바뀌어 숫자가 됨.그리고 256으로 나눠진다. 그 결과가 list로 출력돼고 vals에 들어감.
            images.append(vals) #images 로 값들이 들어감.
    return {"labels":labels, "images":images} # "labels"로 값을 부를 수 있음, load_csv(fname)쓰면 labels, images 둘다 한꺼번에 부르게 됨 그래서 이름을 붙여서 따로 부를 수 있게.
data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

#학습하기
clf = svm.SVC()
clf.fit(data["images"], data["labels"])

#예측하기
predict = clf.predict(test["images"])

#결과 확인하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률=", ac_score)
print("리포트 =")
print(cl_report)
                          
