import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open("./2BEXXX01.txt","r",encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + "  "
print('코퍼스의 길이: ', len(text))

#문자를 하나하나 읽어 들이고 ID 붙이기
chars = sorted(list(set(text)))
print('사용되고 있는 문자의 수: ', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자 --> ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID --> 문자

#text="안녕하십니까 이지혜입니다
#chars = sorted(list(set(text)))
#char_indices = dict((c, i) for i, c in enumerate(chars))
#indices_char = dict((i, c) for i, c in enumerate(chars))
#char_indices
#{' ': 0, '까': 1, '녕': 2, '니': 3, '다': 4, '십': 5, '안': 6, '이': 7, '입': 8, '지': 9, '하': 10, '혜': 11}
#indices_char
#{0: ' ', 1: '까', 2: '녕', 3: '니', 4: '다', 5: '십', 6: '안', 7: '이', 8: '입', 9: '지', 10: '하', 11: '혜'}

#텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20 #20개의 글자 다음의 한 글자를 저장하고
step = 3    #3글자 건너뛰고 다시 20개 글자 다음의 한 글자를 저장하고를 무한루트
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step): #20-8,3 =--> (12,17)
    sentences.append(text[i: i + maxlen])  #'안녕하십니까 이' (8글자) / (3글자)인 안녕하 가 없어지고, '십니까 이지혜입'(8글자)
    next_chars.append(text[i + maxlen])    # '지'                     / '니' 
print('학습할 구문의 수:', len(sentences)) # sentences = ['안녕하십니까 이', '십니까 이지혜입']
print('텍스트를 ID 벡터로 변환합니다...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool) #np.zeros(5) = [0., 0., 0., 0., 0.] np.zeros(5, dtype=np.bool) = [False, False, False, False, False, dtype=np.bool]
y = np.zeros((len(sentences), len(chars)), dtype=np.bool) #np.zeros((2,2)) = array([[0., 0.],                            np.zeros((2,3,5))
                                                          #                         [0., 0.]])  이렇게 행렬이 됨.                                  array([[[0., 0., 0., 0., 0.],
                                                          #                                                                                                [0., 0., 0., 0., 0.],
                                                          #                                                                                                [0., 0., 0., 0., 0.]],                                                                                                   
                                                          #np.zeros((행,열))
                                                          #                                                                                                [[0., 0., 0., 0., 0.],
                                                          #                                                                                                 [0., 0., 0., 0., 0.],
                                                          #                                                                                                 [0., 0., 0., 0., 0.]]])
for i, sentence in enumerate(sentences):          #v={34,22,39} for i, v in enumerate(t): print("index : {}, value: {}".format(i,v)) 
    for t, char in enumerate(sentence):           #                     ===> index:0,value:34 / index :1,value:22 / index :2,value:39
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

#모델 구축하기(LSTM)----생략
print('모델을 구축합니다...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy',optimizer=optimizer)

#후보를 배열에서 꺼내기
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    prodas = np.random.multinomial(1, preds, 1)
    return np.argmax(preds)

#학습시키고 텍스트 생성하기 반복
for iteration in range(1,60):
    print()
    print('-' * 50)
    print('반복 =', iteration)
    model.fit(X,y,batch_size=128,nb_epoch=1)
    #임의의 시작 텍스트 선택하기
    start_index = random.randint(0, len(text) - maxlen - 1)
    #다양한 다양성의 문장 생성
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('---- 다양성 =  ' , diversity)
        generated = ''
        sentence =  text[start_index: start_index + maxlen] #랜덤으로 시작점부터 해서 20글자를 뽑음. #ex) 피하여 방랑하다가 백부인 우관선사를
        generated += sentence #ex) 피하여 방랑하다가 백부인 우관선사를
        print('---- 시드 = "' + sentence + '"')
        sys.stdout.write(generated)
        #시드를 기반으로 텍스트 자동 생성
        for i in range(400):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
            #다음에 올 문자를 예측하기
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index] #ex) 피하여 방랑하다가 백부인 우관선사를 ? 나올 것같은 '?'을 예측해서 추가한 후에
            #출력하기
            generated += next_char #한글자 추가
            sentence = sentence[1:] + next_char ##ex) 앞에 '피' 가 없어지면서 '하여 방랑하다가 백부인 우관선사를?' 이렇게 ?가 추가한다. 이후에 이것을 반복. 400번 반복해서 420글자가 만들어짐.
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
