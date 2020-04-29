from bayes import BayesianFilter

bf = BayesianFilter()


#텍스트 학습
bf.fit("파격 세일 - 오늘까지만 30% 할인", "광고")
print(bf.words)
print(bf.category_dict)
print(bf.word_dict)

print("=-=-=-=-=-=-=--=-=-=-=-=--=")

#예측
pre, scorelist = bf.predict("재고 정리 할인, 무료 배송")
print("결과 =",pre)
print(scorelist)
