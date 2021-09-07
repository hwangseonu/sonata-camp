from tkinter import *


class LoginPage(Tk):
    def __init__(self, on_login):
        super().__init__()
        self.on_login = on_login
        self.canvas = Canvas(self, width=300, height=600)
        self.canvas.winfo_toplevel().title('login')
        self.canvas.pack()

        self.input_id = Entry(self.canvas)
        self.input_pw = Entry(self.canvas, show='●')
        self.btn_login = Button(self.canvas, text='login',
                                command=self.on_push_login_btn)

        self.canvas.create_text(70, 300 - 15, text='username')
        self.canvas.create_text(70, 300 + 15, text='password')
        self.canvas.create_window(150, 300 + 60, window=self.btn_login)
        self.canvas.create_window(150 + 30, 300 - 15, window=self.input_id)
        self.canvas.create_window(150 + 30, 300 + 15, window=self.input_pw)

    def on_push_login_btn(self):
        self.on_login(self.input_id.get(), self.input_pw.get())
        self.destroy()
