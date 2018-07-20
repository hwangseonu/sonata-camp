from tkinter import *


def login_page(service):
    main = Tk()
    canvas = Canvas(main, width=300, height=600)
    canvas.winfo_toplevel().title('login')
    canvas.pack()
    input_id = Entry(canvas)
    input_pw = Entry(canvas, show='●')
    btn_login = Button(canvas, text='login', command=login_btn_click(main, service, input_id, input_pw))

    canvas.create_text(50, 300 - 15, text='username')
    canvas.create_text(50, 300 + 15, text='password')
    canvas.create_window(150, 300 + 60, window=btn_login)
    canvas.create_window(150 + 30, 300 - 15, window=input_id)
    canvas.create_window(150 + 30, 300 + 15, window=input_pw)
    main.mainloop()


def login_btn_click(main, service, input_id, input_pw):
    def check():
        service.login(input_id.get(), input_pw.get())
        main.destroy()
    return check
