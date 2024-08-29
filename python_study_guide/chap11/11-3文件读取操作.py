def my_read(filename):
    # 打开
    file=open(filename,'w+',encoding='utf-8')
    # 操作
    file.write('你好吗') # 写入完成，文件的指针在最后
    # seek 修改文件指针的位置
    file.seek(0)
    # 读取
    #s=file.read() 读取全部
    #s=file.read(2)  # 你好，2指的是2个字符
    #s=file.readline() # 读取一行数据
    #s=file.readline(2) # 读取一行数据中的两个字符
    #s=file.readlines() # 读取所有，列表中的一个元素，s为列表类型
    # 读取“好啊”
    file.seek(3) # 3个字节，一个中文占3个字节，utf-8
    s=file.read() # 读取全部
    print(type(s),s)


    # 关闭
    file.close()

if __name__ == '__main__':
    my_read('d.txt')


