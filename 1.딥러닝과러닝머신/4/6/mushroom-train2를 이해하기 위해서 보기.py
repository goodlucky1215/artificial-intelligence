import pandas as pd

member = ['라이언', '무지', '콘', '프로도', '제이지', '네오', '어피치']
weight = ['30', '25', '5', '20', '25', '15', '20']
age = ['5', '4', '10', '3', '7', '6', '11']

kakao_friends = pd.DataFrame()
kakao_friends['member'] = member
kakao_friends['weight'] = weight
kakao_friends['age'] = age


#위에 표는 이런 느낌이야

# 	member	weight	age
# 0	라이언	30	5
# 1	무지	25	4
# 2	콘	5	10
# 3	프로도	20	3
# 4	제이지	25	7
# 5	네오	15	6
# 6	어피치	20	11

#for row_index, row in kakao_friends.iterrows(): 이 순서도 굉장히 중요함
#만약 for row, row_index in kakao_friends.iterrows(): 이렇게 적는다면
#역할도 그냥 반대로 바뀌는 거임. 무조건 앞에는 0~6이라는 자리만 알려줌
for row_index, row in kakao_friends.iterrows():
    #이는 자리수 즉 0,1,2,3 이런 자리수
    print(row_index)
    #열 중에서도 첫 열인데 하나씩 꺼냄 즉 라이언 꺼내고
    #for col, v in enumerate(row.ix[1:]): 로 들어갔다가
    #다시 올라와서 무지를 꺼냄
    print(row.ix[0])
    for col, v in enumerate(row.ix[1:]):
        print("안으로")
        #라이언의 print(col)= 0 번째의 row.ix[1:]이라서 print(v) = 30, 을 꺼내고
        #라이언의 print(col)= 0 번째의 row.ix[1:]이라서 print(v) = 5 를 꺼내고
        print(col)
        print(v)
        #다시 위로 가서 무지에 관해서 꺼냄

label = []
data = []
attr_list = []


for row_index, row in kakao_friends.iterrows():
    for col, v in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {"dic":{},"cnt":0} #attr["dic"]={}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        if v in attr["dic"]:
            idx = attr["dic"][v]
            print("dfsdf=",v)
            print(attr["dic"])
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            print("dsgfsdf",idx)



