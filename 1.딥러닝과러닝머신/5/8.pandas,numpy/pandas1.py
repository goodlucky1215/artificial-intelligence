import pandas as pd


#애는 열과 행의 테이블 레이블을 출력
a= pd.DataFrame([
    [10,20,30],
    [1,2,3],
    [100,200,300]
])

print(a)


#1차원 데이터 출력에는 시리즈를 사용
s= pd.Series([1.0,3.0,5.0,7.0,9.0])

print(s)
