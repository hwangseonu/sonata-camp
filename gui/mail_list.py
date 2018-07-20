from tkinter import *


def mail_list_page(service):
    main = Tk()
    canvas = Canvas(main, width=100, height=100)
    canvas.pack()
    canvas.winfo_toplevel().title('mails')
    mails = service.get_all_mail()
    btns = []

    for i, mail in enumerate(mails):
        btns.append(Button(canvas, text=f'{mail.title} : {mail.content[:10].rstrip()}...',
                           command=btn_mail_click(service, mail)))
        btns[i].grid(row=i, column=0)
        btns[i].configure(width=100)

    main.mainloop()


def btn_mail_click(service, mail):
    def download():
        for a in mail.attached:
            service.driver.get(a)
    return download
