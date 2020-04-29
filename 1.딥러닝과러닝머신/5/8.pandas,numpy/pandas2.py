import pandas as pd

#키, 몸무게, 유형 데이터 프레임 생성하기
tbl = pd.DataFrame({
    "weight":[80,70.4,65.6,52.6,59.8],
    "height":[182,176,172,165,168],
    "type":['f','n','n','t','n']
})

#몸무게 목록 추출(열의 데이터로 추출)
print("몸무게 목록")
print(tbl["weight"])
print(tbl[["weight"]])

#몸무게와 키 목록 추출하기
print("  몸무게와 키 목록")
print(tbl[["weight","height"]])
