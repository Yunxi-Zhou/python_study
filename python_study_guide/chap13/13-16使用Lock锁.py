import threading 
from threading import Thread,Lock
import time

ticket=50 # 代表的是50张票
lock_obj=Lock()

def sale_ticket():
    global ticket

    # 每个排队窗口假设有100人
    for i in range(100):  # 每个线程要执行100次循环
        lock_obj.acquire()
        if ticket>0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket-=1
        time.sleep(1)
        lock_obj.release()


if __name__ == '__main__':
    for i in range(3):  #创建三个线程，代表3个窗口
        t=Thread(target=sale_ticket)
        t.start() # 启动程序
        