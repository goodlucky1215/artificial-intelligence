from selenium import webdriver
USER= "goodlucky00"
PASS= "9867qhrja"


#phantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

#로그인 페이지 접근하기
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

#텍스트 박스에 아이디와 비밀번호 입력하기
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)
browser.save_screenshot("Website_d.png")

#입력 양식 전송해서 로그인하기
button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()
browser.save_screenshot("Website_r.png")

#메일 페이지 데이터 가져오기
browser.get("https://mail.naver.com/")
browser.save_screenshot("Website_f.png")

#메일 목록 출력하기
titles= browser.find_elements_by_css_selector("strong.mail_title")
print(titles)
for title in titles:
    print("-",title.text)
    
