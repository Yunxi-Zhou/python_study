import os
print('当前路径:',os.getcwd())
lst=os.listdir()
print('当前路径所有目录和文件',lst)
print('指定路径/Users/xianhuiliu/Documents下所有目录和文件',os.listdir('/Users/xianhuiliu/Documents'))
# 创建目录
#os.mkdir('好好学习')   如果创建的文件夹存在程序报错

#os.makedirs('./aa/bb/cc')  创建多个目录

# 删除目录

#os.rmdir(('./好好学习'))  删除的目录不存在，报错

#os.removedirs('./aa/bb/cc')  删除多个目录

# 改变当前的工作路径
os.chdir('/Users/xianhuiliu/Documents/python_project/chap11')
print('当前的工作路径',os.getcwd())  # 再写代码，工作路径就是chap11

# 遍历目录树，相当于递归
for dirs,dirlst,filelst in os.walk('/Users/xianhuiliu/Documents/python_project'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('-----------------')

