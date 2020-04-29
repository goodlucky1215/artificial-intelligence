from sklearn import svm, metrics
import glob, os.path, re, json

files = glob.glob("./train/*") #  glob는 파일들의 목록을 뽑을 때 사용, glob.glob("./train/*.txt") txt를 붙이면 txt 파일만 불러옴
train_data = []
train_label = []
for file_name in files:
    #레이블 구하기
    basename = os.path.basename(file_name) #os.path는 경로를 포함하지 않고 파일 목록을 뽑고,
                                           #glob는 경로를 포함하고 파일 목록을 뽑는다.
    lang = basename.split("-")[0] # "-"로 나눠서 [0] 언어 부분만을 가지는 lang을 만듬.

    #텍스트 구하기
    #with를 사용하면 open~close를 한 줄로 해결할 수 있다.
    file = open(file_name, "r" , encoding = "utf-8")
    text = file.read()
    text = text.lower() #텍스트 내부에 있는 것을 lower로 인해서 소문자로 변환
    file.close()

    #알파벳 출현 빈도 구하기
    code_a = ord("a") #ord는 각각의 문자cha을 숫자로 바꿔 줌.
    code_z = ord("z")
    count = [0 for n in range(0,26)]# 0 이 26개가진 list를 만
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1 #code_current - code_a를 해주면 각 자리에 문자가 나오는 수에 +1이 더해져서 그 문자가 몇 번 나오는지 count가 됨.

    # print(lang, count) 이걸로 하면 벡터(0~1)안돼므로 정규화가 필요
    total = sum(count)
    count = list(map(lambda n: n / total, count))

    #리스트에 넣기
    train_label.append(lang)
    train_data.append(count)


files = glob.glob("./test/*") #  glob는 파일들의 목록을 뽑을 때 사용, glob.glob("./train/*.txt") txt를 붙이면 txt 파일만 불러옴
test_data = []
test_label = []
for file_name in files:
    #레이블 구하기
    basename = os.path.basename(file_name) #os.path는 경로를 포함하지 않고 파일 목록을 뽑고,
                                           #glob는 경로를 포함하고 파일 목록을 뽑는다.
    lang = basename.split("-")[0] # "-"로 나눠서 [0] 언어 부분만을 가지는 lang을 만듬.

    #텍스트 구하기
    #with를 사용하면 open~close를 한 줄로 해결할 수 있다.
    file = open(file_name, "r" , encoding = "utf-8")
    text = file.read()
    text = text.lower() #텍스트 내부에 있는 것을 lower로 인해서 소문자로 변환
    file.close()

    #알파벳 출현 빈도 구하기
    code_a = ord("a") #ord는 각각의 문자cha을 숫자로 바꿔 줌.
    code_z = ord("z")
    count = [0 for n in range(0,26)]# 0 이 26개가진 list를 만
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <= code_z:
            count[code_current - code_a] += 1 #code_current - code_a를 해주면 각 자리에 문자가 나오는 수에 +1이 더해져서 그 문자가 몇 번 나오는지 count가 됨.

    # print(lang, count) 이걸로 하면 벡터(0~1)안돼므로 정규화가 필요
    total = sum(count)
    count = list(map(lambda n: n / total, count))

    #리스트에 넣기
    test_label.append(lang)
    test_data.append(count)

#학습시키기
clf = svm.SVC()
clf.fit(train_data,train_label)
predict = clf.predict(test_data)
score = metrics.accuracy_score(test_label,predict)
print("score=",score)
report = metrics.classification_report(test_label, predict)
print("report=",report)

    
