from konlpy.tag import Twitter
twitter = Twitter()
malist=twitter.pos("아버지 가방에 들어가신다.ㅋㅋㅋㅋ",norm=True,stem=True)
print(malist)

#morphs 형태소를 다 짤라서 줌
print(twitter.morphs("단독입찰보다 복수입찰의 경우"))

#nouns 단어(명사)만 줌
print(twitter.nouns("유일하게 항공기 체계 종합개발 경험을 갖는 kil는"))

#pos 형태소를 다 짤라서 형태소의 종류까지 알려줌
print(twitter.pos("이것도 돼나욬?ㅋ"))
#pos norm은 ㅋㅋ까지 변환
print(twitter.pos("이것도 돼나욬?ㅋ",norm=True))
#pos stem을 쓰면 욬 --> 요 로 맞는 글자로 변경
print(twitter.pos("이것도 돼나욬?ㅋ",norm=True,stem=True))

