from provider.naver import NaverMailProvider
from gui.login import LoginPage
from tkinter import messagebox

from gui.main import MainPage


def on_login(username, password):
    global provider
    try:
        provider.login(username, password)
    except RuntimeError as err:
        messagebox.showinfo('Error', err)
        exit(-1)


if __name__ == '__main__':
    provider = NaverMailProvider()
    login = LoginPage(on_login)
    login.mainloop()

    main = MainPage(provider)
    main.mainloop()
