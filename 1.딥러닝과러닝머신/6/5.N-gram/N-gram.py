#레벤슈타인 거리 구하기
def calc_distance(a,b):
    '''레벤슈타인 거리 계산하기'''
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "":return b_len # a 가 비어있다면, b_len의 길이만큼 채워지니깐 그 횟수가 됨.
    if b == "":return a_len # b 가 비어있다면, a_len의 길이만큼 채워지니깐 그 횟수가 됨.
    # 2차원 표 (a_len+1, b_len+1) 준비하기
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1): #0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]
    #0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[j][0] = j
    #표 채우기
    for i in range(1, a_len+1):
        ac = a[i-1]
        for j in range(1, b_len+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,      #문자 삽입
                matrix[i][j-1] + 1,      #문자 제거
                matrix[i-1][j-1] + cost  #문자 변경
            ])
   #print(matrix)
    return matrix[a_len][b_len]

# "가나다라" 와 "가마바라" 의 거리
print(calc_distance("가나다라","가마바"))
#파악해보면,
#a_len = 4 , b_len = 3
#matrix = [[], [], [], [], []]로 채워짐
#matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]
#matrix[0][0] = 0 / matrix[1][0] = 1 / matrix[2][0] = 2 / matrix[3][0] = 3 / matrix[4][0] = 4
#matrix[0][0] = 0 / matrix[1][0] = 1 / matrix[2][0] = 2 / matrix[3][0] = 3
#ac= a[0] = 가 / bc=b[0] = 가 / ac == bc 므로 cost= 0
#matrix[0][0] = min([matrix[0][1] + 1,matrix[1][0] + 1, matrix[0][0] + 0]) = min(1,2,0) = 0
#ac= a[0] = 가 / bc=b[1] = 마 / ac와bc 같지않므로 cost= 1
#matrix[0][1] = min([matrix[0][2] + 1,matrix[1][1] + 1, matrix[0][1] + 0]) = min(1,1,0) = 0
#이런식으로하면 matrix= [[0, 0, 0, 0], [1, 0, 1, 1], [2, 1, 1, 2], [3, 2, 2, 2], [4, 3, 3, 3]] 가 됨.
#그래서 matrix[a_len][b_len]=matrix[4][3]= 3 이 됨!


#실행 예
samples = ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]   #samples[0]='신촌역'
r = sorted(samples, key = lambda n: calc_distance(base,n))
#sorted는 작은 숫자부터 차례로 정렬하는데 key를 만들어서
#calc_distance(base,n)를 넣어 회수를  저장해서 sorted가 이를 반영해서
#saplese들의 순서를 정렬하게 됌.
#print(r)=['신촌역', '신천역', '신천군', '신발', '마곡역']
for n in r:
    print(calc_distance(base, n), n)
