from selenium import webdriver
from bs4 import BeautifulSoup
import re


class MailService:
    def __init__(self, driver):
        if driver is 'phantomjs':
            self.driver = webdriver.PhantomJS('./phantomjs')
        else:
            self.driver = webdriver.Chrome('./chromedriver')

    # webdriver 를 이용하여 네이버에 로그인합니다.
    def login(self, un, pw):
        try:
            self.driver.get('https://nid.naver.com/nidlogin.login')
            self.driver.find_element_by_id('id').send_keys(un)
            self.driver.find_element_by_id('pw').send_keys(pw)
            self.driver.find_element_by_id('label_login_chk').click()
            self.driver.find_element_by_class_name('btn_global').click()
            return True
        except:
            return False

    # 로그인 된 유저의 메일 중 정규표현식 '\d+ .+'를 만족하는 메일들을 가져옵니다.
    def get_all_mail(self):
        print('get all mains...')  # debug
        self.driver.get('http://mail.naver.com')
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        mails = soup.select('.mTitle')
        result = []

        for m in mails:
            url = m.find('a', {'class': '_d2(mcDragndrop|html5DragStart)'}).get('href')
            mail = self.get_mail(url)
            p = re.compile('\d+ .+')
            if p.match(mail.title):
                print('get', mail.title)  # debug
                result.append(mail)

        return result

    # url 에서 메일의 정보를 파싱하여 객체로 반환합니다.
    def get_mail(self, url):
        url = 'http://mail.naver.com' + url
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        while soup.select_one('title').text.find('메일읽기') is not -1:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        sender = soup.find('a', {'class': '_c1(myContextMenu|showSenderContextLayer|read) _stopDefault'}).text
        title = soup.select_one('.viewTitle').find('h4').text.replace('중요메일로 표시하기', '').strip()
        content = soup.find('div', {'id': 'readFrame'}).text
        attached = []

        save_btns = soup.find_all('a', {'class': 'btn_savepc'})

        if save_btns is not None:
            for b in save_btns:
                attached.append(b.get('href'))

        return Mail(sender, title, content, attached, url)


# 메일의 정보를 가지고 있는 객체입니다.
class Mail:
    def __init__(self, sender, title, content, attached, url):
        self.sender = sender
        self.title = title
        self.content = content
        self.attached = attached
        self.url = url

    def __str__(self):
        return f'{self.sender} {self.title}'
