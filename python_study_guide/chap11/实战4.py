'''

模拟淘宝客服自动回复
淘宝客服为了快速回答买家问题，设置了自动回复的功能，当有买家咨询时，客服自助系统会首先使用提前规划好的内容进行回复

'''

def find_answer(question):
    with open('replay.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline() # 第一次循环  订单
            if line=='':
                break # 退出while
            # 字符串的分割操作
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False
            
if __name__ == '__main__':
    question=input('你的问题是什么:')    
    while True:
        if question=='bye':
            break  # 退出循环
        else:
            # 开始查找答案
            reply=find_answer(question)
            if reply==False:  # 函数返回值为false
                question=input('说啥呢，你的问题是什么:')
            else:
                print(reply)
                question=input('继续，你的问题是什么:')
    print('结束')
