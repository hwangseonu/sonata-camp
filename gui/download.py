from tkinter import *


def download_page(service):
    main = Tk()
    canvas = Canvas(main, width=200, height=100)
    canvas.pack()
    canvas.winfo_toplevel().title('downloading...')
    canvas.create_text(100, 30, text='download')
    canvas.create_window(100, 70, window=Button(canvas, text='download', command=download_all(service, main)))
    download_all(service, main)
    main.mainloop()


def download_all(service, main):
    def download():
        mails = service.get_all_mail()
        for m in mails:
            for a in m.attached:
                service.driver.get(a)
        main.destroy()
    return download
