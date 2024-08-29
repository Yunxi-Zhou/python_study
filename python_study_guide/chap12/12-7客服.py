from socket import socket, AF_INET,SOCK_DGRAM


#1. 创建socket对象
recv_socket=socket(AF_INET,SOCK_DGRAM)

#2. 绑定IP和端口
recv_socket.bind(('127.0.0.1',8888))


while True:
    #3. 接收发送过来的数据
    info,addr=recv_socket.recvfrom(1024)
    print('客户说：',info.decode('utf8'))
    if info.decode('utf-8') =='bye':
        break
    #4. 准备回复数据
    data=input('客服回：')

    # 5. 发送
    recv_socket.sendto(data.encode('utf8'),addr)


    

#6. 关闭
recv_socket.close()










