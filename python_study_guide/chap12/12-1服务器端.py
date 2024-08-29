from socket import socket,AF_INET,SOCK_STREAM
# AF_INET 用于Internet之间的进程通信
# SOCK_STREAM 表示TCP协议

# 1. 创建socket对象
server_socket=socket(AF_INET, SOCK_STREAM)

# 2. 绑定IP地址和端口
ip='127.0.0.1'  #等同于local
port=8888 # port number
server_socket.bind((ip,port))

# 3. 使用listen()开始监听
server_socket.listen(5)

print('服务器启动')

# 4. 等待客户端的连接
client_socket,client_addr=server_socket.accept() # 系列解包赋值

# 5. 接收来自客户端的数据
data=client_socket.recv(1024)
print('客户端发送过来的数据',data.decode('utf-8')) # 要求客户端发过来的数据是使用utf-8编码的

# 6. 关闭socket
server_socket.close()




