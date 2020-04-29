from PIL import Image
import numpy as np

#이미지 데이터를 Averge Hash로 변환하기
def average_hash(fname, size = 16):
    img = Image.open(fname) #이미지 데이터 열기
    img = img.convert('L') #그레이스케일로 변환하기
    img = img.resize((size,size), Image.ANTIALIAS) #리사이즈하기
    pixel_data = img.getdata() #픽셀 데이터 가져오기
    pixels = np.array(pixel_data) #Numpy 배열로 변환하기

    #---------위에까지가 pilow의 역할-------------------
    pixels = pixels.reshape((size, size)) #2차원 배열로 변환하기
    avg = pixels.mean() #평균 구하기
    diff = 1*(pixels > avg) #평균보다 크면 1, 작으면 0으로 변환하기
    return diff

#이전 해시로 변환하기
def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2) #이진수를 정수로 변환하기
        bhash.append("%04x"%i)
    return "".join(bhash)

# Average Hash 출력하기 #이미지 비슷한지 비교하기
ahash1 = average_hash('min.jpg')
ahash2 = average_hash('land0.jpg')
#print((ahash1 != ahash2))
a= ahash1.reshape(1,-1)
b= ahash2.reshape(1,-1)
#print((a != b))
print((a != b).sum())
