import pandas as pd

#키, 몸무게, 유형 데이터 프레임 생성하기
tbl = pd.DataFrame({
    "weight":[80,70.4,65.6,52.6,59.8],
    "height":[182,176,172,165,168],
    "type":['f','n','n','t','n']
})

#부분 출력하기 
print("tbl[2:4]\n", tbl[2:4])
print('\n')
#3번째 이후의 데이터 출력하기
print("tbl[3:]\n",tbl[3:])
print('\n')
#키 170 이상만 뽑기
print("170 이상인 사람\n",tbl[tbl.height >=170])
print('\n')
#체형이 nomal 인사람 뽑기
print("체형이 보통인 사람\n",tbl[tbl.type == 'n'])
print('\n')
#키로 정렬하기
print(tbl.sort_values(by="height"))
print('\n')
#몸무게로 정렬하기
print(tbl.sort_values(by="weight"))
print('\n')
#몸무게로 정렬하기,ascending=False는 무거운 순서대로 정렬
print(tbl.sort_values(by="weight",ascending=False))

