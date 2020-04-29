import numpy as np

#10의 0, float32 자료형 생성
v=np.zeros(10,dtype=np.float32)
print(v)
print('\n')
#연속된 10개의 uint64 자료형 데이터 생성
v=np.arange(10,dtype=np.uint64)
print(v)
print('\n')
#3배곱하기
v *=3
print(v)
print('\n')
#v이 평균 구하기
print(v.mean())
