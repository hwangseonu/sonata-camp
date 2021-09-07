from tkinter import *
import tkinter.messagebox
import functools

from provider.mail import MailProvider, Mail


class MainPage(Tk):
    def __init__(self, provider: MailProvider):
        super().__init__()
        self.provider = provider

        self.resizable(False, False)
        self.container = Frame(self)
        self.canvas = Canvas(self.container, width=300, height=500)
        self.buttons_frame = Frame(self.canvas)
        self.y_scrollbar = Scrollbar(self.container, orient='vertical', command=self.canvas.yview)
        self.canvas.create_window((0, 0), window=self.buttons_frame, anchor='nw')

        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="모든 첨부파일 저장", command=self.download_all)
        self.menubar.add_cascade(label="파일", menu=self.filemenu)
        self.config(menu=self.menubar)

        self.mails = provider.get_mails()

        for mail in self.mails:
            content = mail.content
            content = content if len(mail.content) <= 10 else content[:10] + '...'
            text = f'{mail.title}: {content} [{len(mail.files)}]'
            button = Button(self.buttons_frame, text=text,
                            width=45,
                            command=functools.partial(self.download_one, mail))
            button.pack()

        self.buttons_frame.update()
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set,
                              scrollregion="0 0 0 %s" % self.buttons_frame.winfo_height())

        self.canvas.pack(side=LEFT)
        self.y_scrollbar.pack(side=RIGHT, fill=Y)

        self.container.pack()

    def download_one(self, mail: Mail):
        if len(mail.files) <= 0:
            tkinter.messagebox.showinfo("첨부파일 다운로드", "첨부파일이 없습니다.")
        else:
            self.provider.download_files(mail)
            tkinter.messagebox.showinfo("첨부파일 다운로드", "다운로드가 완료되었습니다.")

    def download_all(self):
        for mail in self.mails:
            self.provider.download_files(mail)
        tkinter.messagebox.showinfo("첨부파일 다운로드", "다운로드가 완료되었습니다.")
