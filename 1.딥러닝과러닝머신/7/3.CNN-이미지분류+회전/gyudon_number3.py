from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

#분류 대상 카테고리 선택하기
caltech_dir = "./image" #image라는 파일
categories = ["ant","brain","chandelier","ibis"] #image 안에 파일이름
nb_classes = len(categories)

#이미지 크기 지정
image_w = 64
image_h = 64
pixels = image_w * image_h * 3 # 3은 RGB값

#이미지 데이터 읽어 들이기
counter = 0
flag =False
X = []
Y = []
for idx, cat in enumerate(categories):
    #레이블 지정
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    #이미지
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg") #glob을 사용하면 파일 안에 있는 이미지를 모두 읽어들일 수 있음. 
    for i,f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w,image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if flag == False:
            img.save("./image/"+str(counter)+".png")
            counter = counter+1
        for angle in range(-20,20,5):#-20 -15 -10......
            #회전 데이터 추가
            img2 = img.rotate(angle)
            data = np.asarray(img2)
            X.append(data)
            Y.append(label)
            if flag == False:
                img2.save("./image/"+str(counter)+".png")
                counter = counter+1
            #반전 데이터
            img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
            data = np.asarray(img2)
            X.append(data)
            Y.append(label)
            if flag == False:
                img2.save("./image/"+str(counter)+".png")
                counter = counter+1
        flag=True
X = np.array(X)
Y = np.array(Y)

#학습 전용 데이터와 테스트 전용 데이터 구분
X_train, X_test, y_train, y_test = \
         train_test_split(X,Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy",xy)

print("ok", len(Y))
        
