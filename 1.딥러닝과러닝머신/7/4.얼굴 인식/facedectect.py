#openCV는 이미지 처리, 구조 분석, 패턴 인식, 머신러닝을 활용한
#이미지와 동영상 처리 등의 다양한 기능을 지원
import cv2
import sys

#입력 파일 지정하기
image_file="naa.jpg"

#캐스케이드 파일의 경로 지정하기
cascade_file="/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"

#이미지 읽어들이기
image = cv2.imread(image_file)
#그레이스케일로 변환하기
image_gs = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#얼굴 인식 특징 파일 읽어 들이기
cascade=cv2.CascadeClassifier(cascade_file)
#얼굴 인식 실행하기
face_list=cascade.detectMultiScale(image_gs,
    scaleFactor=1.1,
    minNeighbors=1,   #
    minSize=(150,150))#150x150 픽셀 이하의 크기는 무시하겠다는 의미

if len(face_list) > 0:
    #인식한 부분 표시하기
    print(face_list) #사각형 틀을 그림
    color = (0, 0, 255) #색깔로 표시(빨간색)
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x,y), (x+w, y+h), color, thickness=8)
    #파일로 출력하기
    cv2.imwrite("facedetect-output.PNG", image)
else:
    print("no face")
                        
