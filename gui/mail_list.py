from tkinter import *


# 모든 메일을 볼 수 있는 창입니다.
def mail_list_page(service):
    print('open mail list')  # debug
    main = Tk()  # 새로운 창을 생성합니다.
    canvas = Canvas(main, width=100, height=100)  # 창의 크기를 100 x 100으로 설정합니다.
    canvas.pack()  # 불필요한 공간을 제거합니다.
    canvas.winfo_toplevel().title('mails')  # 창의 제목을 mails 로 설정합니다.
    mails = service.get_all_mail()  # 과제물 메일을 크롤링 합니다.
    btns = []   # 메일들이 보여질 버틀들입니다.

    if not mails:
        fail = Tk()
        canvas = Canvas(fail, width=200, height=100)
        canvas.pack()
        canvas.winfo_toplevel().title('need login')
        canvas.create_text(100, 50, text='로그인을 먼저 해주세요')
        main.destroy()
        fail.mainloop()

    # enumerate 는 index 와 함께 순회할 수 있도록 해줍니다.
    for i, mail in enumerate(mails):
        # 내용이 10자 이상이면 축약한다.
        if len(mail.content) > 10:
            content = mail.content[:30] + '...'
        else:
            content = mail.content

        btns.append(Button(canvas, text=f'{mail.title}: {content}    -->    클릭 시 다운로드.',
                           command=btn_mail_click(service, mail)))  # 학번 이름 : 내용 일부... (예시. 1101 홍길동 : 과제제출했습니다....)
        btns[i].grid(row=i, column=0)   # 버튼의 grid 를 설정합니다. 보기좋게 배치하기 위함입니다.
        btns[i].configure(width=100)    # 버튼의 크기를 고정합니다.

    main.mainloop()


# 각각의 메일을 클릭하면 실행할 함수를 리턴합니다.
# 함수를 반환하는 이유는 매개변수를 이용하기 때문입니다.
# 메일의 첨부파일들을 다운로드합니다.
def btn_mail_click(service, mail):
    def download():
        for a in mail.attached:
            print('download', a)  # debug
            service.driver.get(a)

        msg = '다운로드 되었습니다.'
        if len(mail.attached) == 0:
            msg = '첨부파일이 없습니다.'
        main = Tk()
        canvas = Canvas(main, width=200, height=100)
        canvas.pack()
        canvas.winfo_toplevel().title('download')
        canvas.create_text(100, 50, text=msg)
        main.mainloop()

    return download
