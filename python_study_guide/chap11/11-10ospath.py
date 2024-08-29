import os.path
print('获取文件的绝对路径：',os.path.abspath('./b.txt'))
print('判断目录或文件在磁盘上是否存在：',os.path.exists('b.txt'))# 相对路径
print('判断目录或文件在磁盘上是否存在：',os.path.exists('new_b.txt'))#False
print('判断目录或文件在磁盘上是否存在：',os.path.exists('./好好学习'))#False
print('拼接路径：',os.path.join('/Users/xianhuiliu/Documents/python_project','b.txt'))
print('分割文件的名和后缀名:',os.path.splitext('b.txt')) # tuple
print('提取文件名:',os.path.basename('/Users/xianhuiliu/Documents/python_project/b.txt'))
print('提取路径:',os.path.dirname('/Users/xianhuiliu/Documents/python_project/b.txt'))

print('判断一个路径是否是有效路径:', os.path.isdir('/Users/xianhuiliu/Documents/python_project')) # True
print('判断一个路径是否是有效路径:', os.path.isdir('/Users/xianhuiliu/Documents/python_project110')) # False

print('判断一个文件是否是有效文件:', os.path.isfile('/Users/xianhuiliu/Documents/python_project/b.txt')) # True
print('判断一个文件是否是有效文件:', os.path.isfile('/Users/xianhuiliu/Documents/python_project/bnn.txt')) # False





