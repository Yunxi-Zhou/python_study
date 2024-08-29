# 存储和读取一维数据
def my_write():
    # 一维数据，列表，元组，集合
    lst=['a', 'b', 'c', 'd', 'e']
    with open('student.csv', 'w') as file:
        file.write(','.join(lst)) # 列表转成字符串

def my_read():
    with open('student.csv', 'r') as file:
        s=file.read()
        lst=s.split(',')  # 字符串转成列表
        print(lst)

# 存储和读取二维数据

def my_write_table():
    lst=[
        ['a', 'b', 'c', 'd', 'e'],
        ['1','2','3','4','5'],
        ['b', 'b', 'd', 'd', 'e'],
    ]
    with open('table.csv','w') as file:
        for item in lst: # item的数据类型是列表
            line=','.join(item)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]  # 存储读取数据
    with open('table.csv','r') as file:
        lst=file.readlines()  # 每一行是列表中的一个元素
        print(type(lst),lst)
        for item in lst:  # item是字符串类型
            new_lst=item[:len(item)-1].split(',')
            data.append(new_lst)
    print(data)





if __name__ == '__main__':
    #my_write()
    my_read()
    #my_write_table()
    my_read_table()
