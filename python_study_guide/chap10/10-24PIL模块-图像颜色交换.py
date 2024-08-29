
#Pillow

from PIL import Image

# 加载图片
im = Image.open('selfphoto.jpg')
#print(type(im),im)

# 提取RGB图像的颜色通道，返回结果是图像的副本

r,g,b = im.split()


# 合并通道
om = Image.merge(mode='RGB',bands=(r,b,g))
om.save('new_selfphoto.jpg')







