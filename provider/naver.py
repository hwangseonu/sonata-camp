from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pyperclip
import time

from provider.mail import Mail, MailProvider


class NaverMailProvider(MailProvider):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome('./chromedriver')

    def login(self, username, password):
        # try:
        #     self.driver.get('https://nid.naver.com/nidlogin.login')
        #     self.driver.find_element_by_id('id').send_keys(username)
        #     self.driver.find_element_by_id('pw').send_keys(password)
        #     self.driver.find_element_by_id('log.login').click()
        #     if self.driver.page_source.find('아이디 또는 비밀번호가 잘못 입력 되었습니다') != -1:
        #         return False
        #     return True
        # except:
        #     return False

        # 주석 처리된 내용은 캡챠에 의해 막혔습니다.
        # 아이디와 패스워드를 클립보드에 저장하여 붙여넣기 하는 것으로 우회합니다.

        self.driver.get('https://nid.naver.com/nidlogin.login')

        input_id = self.driver.find_element_by_id('id')
        input_pw = self.driver.find_element_by_id('pw')

        input_id.click()
        pyperclip.copy(username)
        input_id.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.1)

        input_pw.click()
        pyperclip.copy(password)
        input_pw.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.1)

        self.driver.find_element_by_id('log.login').click()
        time.sleep(0.1)

        if self.driver.page_source.find('아이디 또는 비밀번호가 잘못 입력 되었습니다') != -1:
            raise RuntimeError('아이디 또는 비밀번호가 잘못 입력 되었습니다')

    def get_mails(self) -> [Mail]:
        self.driver.get('https://mail.naver.com/')
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        mails = soup.select('.mailList .mTitle')
        result = []

        for mail in mails:
            url = mail.find('a', {'class': '_d2(mcDragndrop|html5DragStart)'}).get('href')
            mail = self.get_mail(url)
            p = re.compile(r'\d{5}\s[가-힣]{2,5}')
            if p.match(mail.title):
                result.append(mail)
        return result

    def get_mail(self, url) -> Mail:
        url = 'https://mail.naver.com/' + url
        self.driver.get(url)
        time.sleep(0.1)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        sender = soup.find('a', {'class': '_c1(myContextMenu|showSenderContextLayer|read) _stopDefault'})

        view_title = soup.select_one('.viewTitle')
        title = view_title.find('h4').text.replace('중요메일로 표시하기', '').strip()
        content = soup.find('div', {'id': 'readFrame'}).text.strip()
        files = []

        save_btns = soup.find_all('a', {'class': 'btn_savepc'})

        for b in save_btns:
            files.append(b.get('href'))

        return Mail(sender, title, content, files, url)

    def download_files(self, mail: Mail):
        for file in mail.files:
            self.driver.get(file)
