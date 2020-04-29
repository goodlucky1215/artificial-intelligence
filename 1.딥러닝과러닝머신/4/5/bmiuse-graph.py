import matplotlib.pyplot as plt
import pandas as pd

#pandas로 CSV 파일 읽어드리기
tbl=pd.read_csv("bmi.csv", index_col=2) #???만약 테이블 내의 특정한 열을 행 인덱스로 지정하고 싶으면 index_col 인수를 사용한다.

#그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"],b["height"],c=color,label=lbl)

scatter("fat", "red")
scatter("normal","yellow")
scatter("thin", "purple")

ax.legend()
plt.savefig("bmi-test.png")
               
