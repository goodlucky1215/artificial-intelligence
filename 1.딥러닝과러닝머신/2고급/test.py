
from selenium import webdriver


url="https://www.naver.com/"

#phantomjs 드라이버 추출
browser = webdriver.PhantomJS()

#3초대기
browser.implicitly_wait(3)

#URL 들어가기
browser.get(url)

#화면 캡쳐 후 저장
browser.save_screenshot("Website.png")


#브라우저 종료
browser.quit()
