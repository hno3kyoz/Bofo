# -*- coding: cp936 -*-
from tkinter import *

root = Tk()
root.title("�����ѯ")
root.geometry('300x300')  # ��x ����*

l1 = Label(root, text="�˻���")
l1.pack()  # �����side���Ը�ֵΪLEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
xls = Entry(root, textvariable=xls_text)
xls_text.set(" ")
xls.pack()

l2 = Label(root, text="E-mail��")
l2.pack()  # �����side���Ը�ֵΪLEFT  RTGHT TOP  BOTTOM
sheet_text = StringVar()
sheet = Entry(root, textvariable=sheet_text)
sheet_text.set(" ")
sheet.pack()

l3 = Label(root, text="��")
l3.pack()  # �����side���Ը�ֵΪLEFT  RTGHT TOP  BOTTOM
loop_text = StringVar()
loop = Entry(root, textvariable=loop_text)
loop_text.set(" ")
loop.pack()




def on_click():
    x = xls_text.get()
    s = sheet_text.get()
    l = loop_text.get()
    string = str("xls����%s sheet����%s ѭ��������%s ����ʱ�䣺%s " % (x, s, l, sl))
    print("xls����%s sheet����%s ѭ��������%s ����ʱ�䣺%s " % (x, s, l, sl))
    messagebox.showinfo(title='aaa', message=string)


Button(root, text="press", command=on_click).pack()

root.mainloop()