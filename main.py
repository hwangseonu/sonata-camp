from crawler.mail import MailService
from gui.main import main_page

# 메일을 크롤링하기 위한 객체입니다. 하나의 객체만 사용되기 때문에 다른 곳에 매개변수로 전달합니다.
print('start You Must Submit')
service = MailService('chrome')
main_page(service)
print('end')
