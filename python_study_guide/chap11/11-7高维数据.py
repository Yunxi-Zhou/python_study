import json
# 准备高维
lst=[
    {'name':'Test1', 'value':30, 'type':100},
    {'name':'Test2', 'value':40, 'type':90},
    {'name':'Test3', 'value':20, 'type':75}
]

# 
s=json.dumps(lst,ensure_ascii=False,indent=4) # ensure——ascii正常显示中文，indent增加数据的缩进，JSON格式的字符串更具有可读性
print(type(s))  # 编码 list-->str
print(s)

# 解码

lst2=json.loads(s)
print(type(lst2))
print(lst2)

# 编码到文件中
with open('test1.txt','w') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

# 解码到程序
with open('test1.txt','r') as file:
    lst3=json.load(file)  # 直接是列表类型
    print(type(lst3))
    print(lst3)


