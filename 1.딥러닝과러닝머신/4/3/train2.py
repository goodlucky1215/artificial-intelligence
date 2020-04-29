from sklearn import model_selection, svm, metrics
import pandas

train_csv = pandas.read_csv("./mnist/train.csv",header=None)  #./minst/안에 있다, header가 둘다 없기 때문에 None으로 표시
tk_csv = pandas.read_csv("./mnist/t10k.csv",header=None)


#최대255의 숫자를 가지는 퍼일이라서, 이들은 나눠서 0~1 사이로 바꿔줘야함.
def test(ㅣ):
    output = []
    for i in ㅣ:
        output.append(float(i) / 256)
    return output
                                                             #map(변환하고 싶은 지정된 함수로 처리, 변환하고 싶은 값)
                                                             #map겉에 list를 넣어서 list의 함수로!!
train_csv_data = list(map(test, train_csv.iloc[:,1:].values)) #iloc[행의 시작과 끝 표시, 열의 시작과 끝 표시]
tk_csv_data = list(map(test, tk_csv.iloc[:,1:].values))     #0번째 열은 lable로 지정해서 빼줘야 하므로.
print(tk_csv_data)

train_csv_lable = train_csv[0].values #첫번째 열(세로)를 쫙 lable 함을 의미
tk_csv_lable = tk_csv[0].values

clf = svm.SVC()
clf.fit(train_csv_data, train_csv_lable)
predict = clf.predict(tk_csv_data)
score = metrics.accuracy_score(tk_csv_lable, predict)
print("정답률=", score)
