def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('你好啊')


def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
        print(file.read())


def copy_fun(src_file, target_file):
    with open(src_file,'r',encoding='utf-8') as file:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file.read()) # 将读取内容直接写进文件


if __name__ == '__main__':
    write_fun()
    read_fun()
    # 文件复制
    copy_fun('./aa.txt','./dd.txt')