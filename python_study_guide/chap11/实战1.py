''' 
在指定路径下批量创建3000份文本文件，文件名格式为序号_物资类别_用户识别码组成
序号0001-3000
水果，烟酒，粮油，肉蛋，蔬菜
用户识别码为9位的随机十六进制数 
'''
import random 
import os
import os.path
# 函数式编程

def create_filename():
    filename_lst=[]
    lst=['水果','烟酒','粮油','肉蛋','蔬菜']  # 物资类别
    code=['0','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(1,3001):
        filename=''
        # 拼接文件
        if i <10:
            filename+='000'+str(i)
        elif i < 100:
            filename+='00'+str(i)
        elif i < 1000:
            filename+='0'+str(i)
        else:
            filename+=str(i)
        # 拼接物资类别
        filename+='_'+random.choice(lst)
        # 拼接识别码
        s=''
        for j in range(9):  # 循环的作用是次数
            s+= random.choice(code)
        filename+='_'+s
        filename_lst.append(filename)
    return filename_lst
    
# 创建文件的函数

def create_file(filename):
    with open(filename,'w') as file:
        pass



if __name__=='__main__':
    # 在指定的路径下创建文件
    path='./data'
    if not os.path.exists(path):
        os.mkdir(path)
    lst=create_filename() # 调用获取文件名
    for item in lst:
        create_file(os.path.join(path,item)+'.txt')
    #print(create_filename())
            