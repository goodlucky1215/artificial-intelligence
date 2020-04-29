filename = "a.bin"
data=100

with open(filename,"wb") as f:
    f.write(bytearray([data]))


#텍스트 데이터는 문자 데이터 영역으로 우리가 시각적으로 의미 확인 가능,
#바이너리 데이터는 문자 영역 외 사용으로 시각적으로 의미 확인 안됌.
#바이너리 데이터는 대신 크기가  작음.    
