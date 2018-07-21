from tkinter import *


# login 페이지 입니다.
def login_page(service):
    print('open login window')  # debug
    main = Tk()  # 새로운 창을 띄웁니다.
    canvas = Canvas(main, width=300, height=600)  # 창의 크기를 300 x 600 으로 설정합니다.
    canvas.winfo_toplevel().title('login')  # 창의 제목을 login 으로 설정합니다.
    canvas.pack()  # 창에서 남는 공간을 정리합니다.
    input_id = Entry(canvas)  # id 를 입력할 공간입니다.
    input_pw = Entry(canvas, show='●')  # password 를 입력할 공간입니다. 입력된 값이 가려집니다.
    btn_login = Button(canvas, text='login', command=login_btn_click(main, service, input_id, input_pw))

    canvas.create_text(50, 300 - 15, text='username')
    canvas.create_text(50, 300 + 15, text='password')
    canvas.create_window(150, 300 + 60, window=btn_login)
    canvas.create_window(150 + 30, 300 - 15, window=input_id)
    canvas.create_window(150 + 30, 300 + 15, window=input_pw)
    main.mainloop()


# login 버튼을 클릭하면 실행되는 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용하기 때문입니다.
# 로그인이 완료되면 창을 닫습니다.
def login_btn_click(main, service, input_id, input_pw):
    def check():
        if not service.login(input_id.get(), input_pw.get()):
            fail = Tk()
            canvas = Canvas(fail, width=200, height=100)
            canvas.pack()
            canvas.winfo_toplevel().title('failed login')
            canvas.create_text(100, 50, text='로그인에 실패하였습니다.')
            main.destroy()
            fail.mainloop()
        main.destroy()
        print('login successfully!')  # debug
        print('close login window')  # debug
    return check
