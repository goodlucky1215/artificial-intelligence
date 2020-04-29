from PIL import Image
import numpy as np

with open("min.jpg", "rb") as file: #file 포인트로 이미지 생성
    img = Image.open(file)    #이미지를 오픈
    img = img.convert("RGB")  #색상이 있는 이미지로 변환
    img = img.resize((64,64)) #이미지 크기를 작게 - 왜냐면 오래 걸릴 수 있어서.
    data = np.asarray(img)    #이미지를 데이터로 변환
   #print(data) ---무슨 의미인지 잘 이해가 안가서 list로
   #print(list(data)) ---애도 잘 이해가 안 됨.
    print(len(list(data)))
    print(len(list(data[0])))
    print(data[0][0])
    img.save("test.png")
