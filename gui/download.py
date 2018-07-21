from tkinter import *


# download 버튼을 보여주는 GUI
def download_page(service):
    print('open download window')  # debug
    main = Tk()  # 새로운 창을 띄웁니다.
    canvas = Canvas(main, width=200, height=100)  # 창의 크기를 200 x 100 으로 설정합니다.
    canvas.pack()   # 창에서 남는 공간을 정리합니다.
    canvas.winfo_toplevel().title('downloading...')  # 창의 제목을 downloading... 으로 설정합니다.
    canvas.create_text(100, 30, text='download')
    canvas.create_window(100, 70, window=Button(canvas, text='download', command=download_all(service, main)))
    main.mainloop()


# download 버튼을 클릭하면 실행되는 함수를 반환합니다.
# 함수를 반환하는 이유는 매개변수를 이용하기 때문입니다.
# 크롤링된 모든 메일의 첨부파일을 모두 다운받고 창을 닫습니다.
def download_all(service, main):
    def download():
        print('start download...')  # debug
        mails = service.get_all_mail()
        for m in mails:
            for a in m.attached:
                service.driver.get(a)
        main.destroy()
        print('end download!')  # debug
        print('close download window')  # debug
    return download
