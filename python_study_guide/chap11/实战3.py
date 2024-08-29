'''

记录用户登陆日志并查看
创建xx客服管理系统的登陆界面，每次登陆时，将用户的登陆日志写入文件中，
并且可以在程序中查看用户的登陆日志

'''
import time
def show_info():
    print('输入提示数字，执行相应的操作：0.退出 1.  查看登陆日志')


# 记录日志
def write_loginfo(username):
    with open('log.txt','a',encoding='utf-8') as file:
        s=f'用户名{username},登陆时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')

# 读取日志的操作

def read_loginfo():
    with open('log.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if line=='':
                break
            else:
                print(line)


if __name__ == '__main__':
    #write_loginfo('admin')
    username=input('请输入用户名：')
    pwd=input('请输入pwd：')
    if username=='admin' and pwd =='admin':
        print('success')
        # 将登陆信息写入日志文件
        write_loginfo(username)

        # 提示用户操作
        show_info()
        num=eval(input('请输入想要操作的数字：'))
        while True:
            if num==0:
                print('logged out successfully')
                break # 退出while
            elif num==1:
                print('查看登陆日志：')
                read_loginfo()
                show_info()
            else:
                print('sorry,wrong num')
                show_info()

            num=eval(input('请输入想要操作的数字：'))
    else:
        print('wrong username or pwd')

