#导入socket
# from .... import....
# import .....
import socket
# 创建socket对象
socket_obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定主机ip端口
socket_obj.bind(('127.0.0.1',8889))

# 3. 设置最大连接数量
socket_obj.listen(5)


#4. 等待客户端的TCP连接
client_socket,client_addr=socket_obj.accept()
print('----客户端连接成功----')


# 5. 接收数据
info=client_socket.recv(1024).decode('utf-8')
# while循环的四个步骤，info是初始化变量
while info!='bye':# 条件判断
    if info != '':
        print('接收到的数据是：',info)
    # 准备发送的数据
    data=input('请输入要发送的数据：')

    # 服务器端回复客户端
    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')

# 关闭socket对象
client_socket.close()
socket_obj.close()









