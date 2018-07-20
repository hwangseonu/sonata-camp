from tkinter import *
from gui.login import login_page
from gui.mail_list import mail_list_page
from gui.download import download_page
login = False


def main_page(service):
    main = Tk()
    canvas = Canvas(main, width=400, height=200)
    canvas.winfo_toplevel().title('main page')
    canvas.pack()
    btn_login = Button(canvas, text='login', command=login_click(service))
    btn_mails = Button(canvas, text='show mails', command=mails_click(service))
    btn_download = Button(canvas, text='download all', command=download_click(service))
    btn_close = Button(canvas, text='close', command=close_click(service, main))

    btn_login.config(width=10, height=1)
    btn_mails.config(width=10, height=1)
    btn_download.config(width=10, height=1)
    btn_close.config(width=10, height=1)

    canvas.create_window(50, 100, window=btn_login)
    canvas.create_window(200, 100, window=btn_mails)
    canvas.create_window(350, 100, window=btn_download)
    canvas.create_window(200, 50, window=btn_close)
    main.mainloop()


def mails_click(service):
    def show():
        mail_list_page(service)
    return show


def login_click(service):
    def show():
        login_page(service)
    return show


def download_click(service):
    def show():
        download_page(service)
    return show


def close_click(service, main):
    def close():
        service.driver.close()
        main.destroy()
    return close
