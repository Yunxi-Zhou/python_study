import threading 
from threading import Thread
import time

class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'线程:{threading.currentThread().name}正在执行{i}')


if __name__ == '__main__':
    print('主线程开始')

    # 线程
    lst=[SubThread() for i in range(2)]
    
    for item in lst:  # item的数据类型是Thread类

        # 启动线程
        item.start()

    # 阻塞主线程
    for item in lst:
        item.join()
