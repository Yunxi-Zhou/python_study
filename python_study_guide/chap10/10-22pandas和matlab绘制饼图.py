import pandas as pd
import matplotlib.pyplot as plt

# 读取excel文件

df = pd.read_excel('item_name.xlsx')
# print(df)
# 解决中文乱码

plt.rcParams['font.sans-serif']=['SimHei']

# 设置画布大小
plt.figure(figsize=(10,6))

labels= df['item name']
y = df['bj']

# print(labels)
# print(y)

# 绘制饼图
plt.pie(y,labels=labels, autopct='%1.1f%%',startangle=90)   # 加入九十度角度从｜竖线开始计算，不加入就没有


# 设置x y 轴刻度
plt.axis('equal')
plt.title('bj 2023 item number')

# show results

plt.show()





