import numpy as np
import matplotlib.pyplot as plt
#  png 是四维数组所以不能被numpy 读取
# 读取图片
n1=plt.imread('selfphoto.jpg')
print(type(n1),n1)  # 数组，三维数组，最高位表示图像的高，次高维度表示图像宽，最低维度表示[r,g,b]
plt.imshow(n1)

# 便携一个灰度的公式
n2 = np.array([0.299,0.587,0.114])  # 创建数组
# 将数组n1(rgb)颜色与数组n2(灰度公式固定值),进行点乘运算

x = np.dot(n1,n2)
# 传入数组，显示灰度
plt.imshow(x,cmap='gray')
plt.show()