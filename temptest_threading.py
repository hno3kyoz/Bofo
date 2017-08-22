# import threading, time
#
# def button_on(threadname,delay):
#     while True:
#         print(delay)
#         time.sleep(1)
#
#
# def goon():
#     print('off')
#
# try:
#     threading._start_new_thread(button_on,('thread1',1,))
#     threading._start_new_thread(button_on, ('thread2', 2,))
#
# finally:
#     print('end')


# import threading
# import time
# import inspect
# import ctypes
# import _thread
#
# import bofoshutdown,bofomain
# _thread.start_new_thread(bofomain,)
# _thread.start_new_thread(bofoshutdown)

# import _thread
# import time
#
# def work_thread(id):
#
#     while True:
#         print("Thread ID %d is working" % (id))
#         time.sleep(2)
#
# for i in range(1,2):
#     _thread.start_new_thread(work_thread,(i,))
#
# print("Main thread doing an infinite wait loop...")
#
# while True:
#     time.sleep(2)
#     _thread.exit(work_thread(1))
#     time.sleep(2)
#     _thread.exit(work_thread(2))
#     time.sleep(2)
#     _thread.exit(work_thread(3))
#     pass

import _thread
import time
def a(id):
    print('a starting')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')
    time.sleep(1)
    print('a')



def b(id):
    print('bbbbbb kaishi')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')
    time.sleep(1)
    print('bbbbbb')


_thread.start_new_thread(a, (1,))
time.sleep(5)
_thread.exit(a,1)


_thread.start_new_thread(b, (1,))
time.sleep(3)
_thread.exit()
