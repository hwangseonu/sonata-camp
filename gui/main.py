from tkinter import *
from gui.login import login_page
from gui.mail_list import mail_list_page
from gui.download import download_page


# GUI 의 메인화면 입니다. login, show mails, download all, close 버튼이 있습니다.
def main_page(service):
    main = Tk()  # 새로운 gui 창을 만듭니다.
    canvas = Canvas(main, width=400, height=200)  # 창의 크기를 400 x 200 으로 지정합니다.
    canvas.winfo_toplevel().title('main page')  # 창의 제목을 main page 로 설정합니다.
    canvas.pack()   # 창에서 남는 부분을 제거합니다.
    btn_login = Button(canvas, text='login', command=login_click(service))
    btn_mails = Button(canvas, text='show mails', command=mails_click(service))
    btn_download = Button(canvas, text='download all', command=download_click(service))
    btn_close = Button(canvas, text='close', command=close_click(service, main))

    # 버튼들의 크기를 모두 같게 설정합니다.
    btn_login.config(width=10, height=1)
    btn_mails.config(width=10, height=1)
    btn_download.config(width=10, height=1)
    btn_close.config(width=10, height=1)

    # 버튼들을 추가합니다.
    canvas.create_window(50, 100, window=btn_login)
    canvas.create_window(200, 100, window=btn_mails)
    canvas.create_window(350, 100, window=btn_download)
    canvas.create_window(200, 50, window=btn_close)
    main.mainloop()


# show mails 버튼을 클릭하면 실행할 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용해야하기 떄문입니다.
# 메일의 리스트를 보여줍니다.
def mails_click(service):
    def show():
        mail_list_page(service)

    return show


# login 버튼을 클릭하면 실행할 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용해야하기 떄문입니다.
# login 창을 띄웁니다.
def login_click(service):
    def show():
        login_page(service)

    return show


# download all 버튼을 클릭하면 실행할 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용해야하기 떄문입니다.
# download_page 를 띄웁니다.
def download_click(service):
    def show():
        download_page(service)

    return show


# close 버튼을 클릭하면 실행할 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용해야하기 떄문입니다.
# 화면과 webdriver 를 종료합니다.
def close_click(service, main):
    def close():
        service.driver.close()
        main.destroy()

    return close
