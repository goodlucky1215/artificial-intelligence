#로그인을 위한 모듈 추출하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#아이디와 비밀번호 지정
USER= "goodlucky00"
PASS= "dlwlgp12"

#세션 시작하기
session = requests.session()
#로그인하기
login_info = {
    "m_id": USER, # 아이디 지정
    "m_passwd": PASS #비밀번호 지정
}

url_login = "https://www.66girls.co.kr/member/login.html"
res = session.post(url_login, data=login_info)


#마이페이지 접근하기
url_mypage = "https://www.66girls.co.kr/myshop/mileage/historyList.html"
res = session.get(url_mypage)


#마일리지와 이코인 가져와기
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one("span#xans_myshop_summary_avail_mileage")

print("마일리지: ",soup.select_one("#xans_myshop_summary_avail_mileage").get_text)
