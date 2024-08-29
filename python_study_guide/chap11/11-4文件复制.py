#import os
def copy(src,new_path):
    # 文件的复制就是边读边写的操作
    # 1 打开原文件
    file1=open(src,'rb')
    # 2 打开目标文件
    file2=open(new_path,'wb')
    # 3 开始复制，边读边写
    s=file1.read() # 原文件读取所有
    file2.write(s)  # 向目标文件写入所有

    # 4 关闭
    file2.close()
    file1.close()  # 先打开的后关，后打开的先关


if __name__ == '__main__':
    src='./selfphoto.jpg'  # 代表的是当前目录
    new_path='../chap10/copy_selfphoto.jpg'  # 表示的是上级目录， 相当于windows后退
    #copy(src,new_path)
    #print("当前工作目录:", os.getcwd())
    #print("目录内容:", os.listdir('.'))
    print('success')