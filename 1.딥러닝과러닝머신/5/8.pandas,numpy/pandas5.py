import pandas as pd

#키, 몸무게, 유형 데이터 프레임 생성하기
tbl = pd.DataFrame({
    "weight":[80,70.4,65.6,52.6,59.8],
    "height":[182,176,172,165,168],
    "type":['f','n','n','t','n']
})

#몸무게 키 정규화하기
#최대값 최솟값 구하기
def norm(a,b):
    c=a[b]
    v_max=c.max()
    v_min=c.min()
    print("최대=",v_max,"최소=",v_min)
    a[b] = (c-v_min)/(v_max-v_min)
norm(tbl,"weight")
norm(tbl,"height")
print(tbl)

n=tbl.as_matrix()
print(n)


#*****주의
#머신러닝 라이브러리에 따라 pandas의 dataframe을 지원하지 않는 경우도 있다.
#이럴 때는 numpy 형식으로 변환.
#as_matrix()를 이용하면 numpy의 ndarray 자료형 배열로 변환
