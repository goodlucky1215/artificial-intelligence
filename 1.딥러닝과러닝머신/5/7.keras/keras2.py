#모듈을 읽어 들인다.
from keras.models import Sequential
from keras.layers.core import Dense, Dropout,Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

#데이터를 가공한다.
csv = pd.read_csv("bmi.csv")
csv["weight"] /= 100
csv["height"] /= 200

bmi_class = {
    "thin": [1, 0, 0],
    "normal":[0, 1, 0],
    "fat":[0, 0, 1]
}
#요즘은 보통 입력 데이터를 y 로 표현하고 그 때의 레이블을 x 라고 표현한다!!
y = np.empty((20000,3)) #20000개의 데이터와 list 3개(날씬,보통,뚱뚱)가 들어갈 공간
                        #y = np.empty((20000,3)) =
                        #[
                        #     [빈공강,빈공강,빈공강]
                        #     [빈공강,빈공강,빈공강]
                        #     ....
                        #
                        #     ] 이런식으로 20000만개 만들어짐
                        
for i, v in enumerate(csv["label"]): #enumerate는 csv["label"]이 가진 갯수를 계산 즉 20000을 의미i는 숫자, v는 0부터 차례로 적힌  thin,normal,fat을 가져옴
    y[i] = bmi_class[v]              #y[0]은 따라서 label과 일치하는  bmi_class의 thin,normal,fatd의 [0, 0, 1],[0, 1, 0],[1, 0, 0]을 대입

x = csv[["weight","height"]].as_matrix()

x_train,y_train = x[1:15001], y[1:15001]
x_test, y_test = x[15001:20001], y[15001:20001]

#print(y[0:3])

#[
#   [<키>/200, <몸무게>/100], #0.0~1.0
#   [<키>/200, <몸무게>/100],
#   [<키>/200, <몸무게>/100]
#]

#[
#    'thin',   #[1,0,0]
#    'normal', #[0,1,0]
#    'fat'     #[0,0,1]
#]

#모델을 만든다.
model = Sequential()
model.add(Dense(512,input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
#레이어 형성 compile(self, optimizer, loss, metrics=None, sample_weight_mode=None)
model.compile("rmsprop","categorical_crossentropy",metrics=['accuracy'])
                   
#학습을 시킨다.
model.fit(x_train,y_train)

#예측을 한 뒤: model.predict()
#정답률을 구한다.
score = model.evaluate(x_test, y_test)
print("score:",score)
