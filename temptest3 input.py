# -*- coding: cp936 -*-
from tkinter import *
import os

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
    l1 = xls_text.get()
    l2 = sheet_text.get()
    l3 = loop_text.get()
    # string = str("xls����%s sheet����%s ѭ��������%s ����ʱ�䣺%s " % (x, s, l))
    # print("xls����%s sheet����%s ѭ��������%s ����ʱ�䣺%s " % (x, s, l))
    os.system('cf login -a https://api.system.aws-usw02-pr.ice.predix.io -u ' + l1 + ' -p ' + l2)
    output = os.popen('cf apps')
    print(output.read())

Button(root, text="Check", command=on_click).pack()

root.mainloop()

