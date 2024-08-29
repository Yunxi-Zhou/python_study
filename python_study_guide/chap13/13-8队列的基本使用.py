from multiprocessing import Queue

if __name__ == '__main__':
    # 创建一个队列
    q=Queue(3) # 最多可以接3条信息

    print('队列是否为空:',q.empty())
    print('队列是否为满',q.full())

    # 向队列中添加信息
    q.put('hello')
    q.put('world')

    print('队列是否为空:',q.empty())
    print('队列是否为满',q.full())

    q.put('Python')
    print('队列是否为空:',q.empty())
    print('队列是否为满',q.full())
    # print('队列当中信息个数:',q.qsize())  队列当中信息个数:3


    # 出队
    print(q.get())
    #print('队列当中信息个数:',q.qsize()) 队列当中信息个数:2
    q.put_nowait('html')
    #q.put_nowait('sql')
    #q.put('sql')  # 不会报错，会一直等待，等到队列中有空位置

    # 遍历
    if not q.empty():
        for i in range(3):   # q.qsize() = 3
            print(q.get(block=True))

    print('队列是否为空:',q.empty())
    print('队列是否为满',q.full())
