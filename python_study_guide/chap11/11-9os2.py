import os
# 删除文件
os.chdir('/Users/xianhuiliu/Documents/python_project')
#os.remove('./a.txt')   要删除的文件不存在，报错

# 重命名
#os.rename('./aa.txt','new_aa.txt')




# 转换时间格式

import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(longtime))
    return s

# 获取文件信息
info=os.stat('./new_aa.txt')

print(type(info))
print(info)
print('最近一次访问时间：',date_format(info.st_atime))
print('在mac操作系统中显示文件的创建时间：',date_format(info.st_ctime))
print('最后一次修改时间：',date_format(info.st_mtime))
print('文件的大小(字节)：',info.st_size)


# 启动路径下的文件
#os.startfile('calc.exe')  windows 独有
# 启动Python解释器
#os.startfile('') windows 见台式









