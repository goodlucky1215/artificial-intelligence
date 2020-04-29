import pandas as pd

tbl = pd.DataFrame([
    ["a","b","c"],
    ["Aa","Bb","Cc"],
    ["e","f","g"],
])

print(tbl)
print("--------------")
#행과 열을 반전
print(tbl.T)
