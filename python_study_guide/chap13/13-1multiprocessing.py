from multiprocessing import Process
import os,time
# 函数中的代码是进程要执行的代码
def test():
    print(f'我是子进程,我的PIP是:{os.getpid()},我的父亲是:{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    lst=[]

    # 创建五个子进程
    for i in range(5):
        # 创建子进程
        p=Process(target=test)
        # 启动子进程
        p.start()
        # 启动中的进程添加到列表中
        lst.append(p)

    # 遍历lst，列表中五个子进程
    for item in lst: # item的数据类型是 Process类型
        item.join() # 阻塞主进程

    
    print('主进程执行结束')


