# -*- coding: cp936 -*-
from tkinter import *
import os

root = Tk()
root.title("输入查询")
root.geometry('300x300')  # 是x 不是*

l1 = Label(root, text="账户名")
l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
xls = Entry(root, textvariable=xls_text)
xls_text.set(" ")
xls.pack()

l2 = Label(root, text="E-mail：")
l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
sheet_text = StringVar()
sheet = Entry(root, textvariable=sheet_text)
sheet_text.set(" ")
sheet.pack()

l3 = Label(root, text="区")
l3.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
loop_text = StringVar()
loop = Entry(root, textvariable=loop_text)
loop_text.set(" ")
loop.pack()


def on_click():
    l1 = xls_text.get()
    l2 = sheet_text.get()
    l3 = loop_text.get()
    # string = str("xls名：%s sheet名：%s 循环次数：%s 休眠时间：%s " % (x, s, l))
    # print("xls名：%s sheet名：%s 循环次数：%s 休眠时间：%s " % (x, s, l))
    os.system('cf login -a https://api.system.aws-usw02-pr.ice.predix.io -u ' + l1 + ' -p ' + l2)
    output = os.popen('cf apps')
    print(output.read())

Button(root, text="Check", command=on_click).pack()

root.mainloop()

