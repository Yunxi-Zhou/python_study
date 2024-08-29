
def my_write(s):
    # 打开文件
    file=open('b.txt','a',encoding='utf-8')
    # 操作文件
    file.write(s)
    file.write('\n')
    # 关闭文件
    file.close()

def my_write_list(file,lst):
    # 打开文件
    f=open(file,'a',encoding='utf-8')
    # 操作文件
    f.writelines(lst)
    # 关闭文件
    f.close()

if __name__ == '__main__':
    #my_write('哈哈哈')
    #my_write('你好呀')
    # 准备数据
    lst=['姓名\t','年龄\t','成绩\n','张三\t','30\t','98']
    my_write_list('c.txt',lst)



















