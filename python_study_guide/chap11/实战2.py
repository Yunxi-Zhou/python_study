'''
批量创建文件夹
在指定路径newdir下批量创建指定个数的目录，如果newdir目录不存在，则创建

'''

import os
import os.path

def mkdirs(path,num):
    for item in range(1,num+1):
        os.mkdir(path+'/'+str(item))

    


if __name__ == '__main__':
    path='./newdir'
    if not os.path.exists(path):
        os.mkdir(path)

    num = eval(input('输入需要创建目录个数：'))

    mkdirs(path,num)




